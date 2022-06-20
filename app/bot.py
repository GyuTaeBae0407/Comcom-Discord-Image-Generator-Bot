import os
import sys
import logging
import json

import discord
import requests
from discord import Option, Embed

try:
    from dotenv import load_dotenv

    load_dotenv()
except:
    pass

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
DISCORD_GUILD_ID = os.environ.get("DISCORD_GUILD_ID")
FIREBASE_FUNCS_URL = os.environ.get("FIREBASE_FUNCS_URL")
assert DISCORD_TOKEN is not None, "`DISCORD_TOKEN` is required."
assert DISCORD_GUILD_ID is not None, "`DISCORD_GUILD_ID` is required."
assert FIREBASE_FUNCS_URL is not None, "`FIREBASE_FUNCS_URL` is required."

logger = logging.getLogger(__name__)

# Setup logging
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger.setLevel(logging.INFO)


bot = discord.Bot()


@bot.event
async def on_ready():
    logger.info("We have logged in as {}".format(bot.user))


@bot.slash_command(name="get_task_status")
async def get_task_status(
    ctx: discord.ApplicationContext,
    task_id: Option(str, "task id", required=True),
):
    logger.info("get_task_status")
    try:
        response = requests.post(
            f"{FIREBASE_FUNCS_URL}/getTaskStatus",
            headers={"accept": "application/json", "Content-Type": "application/json"},
            data=json.dumps(
                {
                    "data": {
                        "taskId": task_id,
                    }
                }
            ),
        )
        if response.status_code == 200:
            result = response.json()["result"]
            if result["status"] == "COMPLETED" or result["status"] == "RUNNING":
                logger.info("Task Status is COMPLETED or RUNNING")
                progress = int(result["output"]["progress"])
                image_url = result["output"]["path"]
                embed = Embed(title=f"Task({task_id}) {progress}/100")
                embed.set_image(url=image_url)
                await ctx.respond(embed=embed)
                return
            else:
                logger.info("Task Status is {}".format(result["status"]))
                await ctx.respond(f"[INFO]: Task({task_id})'s status is {result['status']}")
                return
        else:
            response_json = response.json()
            if "error" in response_json and "message" in response_json["error"]:
                await ctx.respond(f"[ERROR]: {response_json['error']['message']}")
                return
            else:
                await ctx.respond(f"[ERROR]: Unknown ERROR")
                return
    except Exception as error:
        logger.error(f"{error}")
        await ctx.respond(f"[ERROR]: {error}")
        return


@bot.slash_command(name="request_task")
async def request_task(
    ctx: discord.ApplicationContext,
    text: Option(str, "text", required=True),
):
    logger.info("request_task")
    try:
        response = requests.post(
            f"{FIREBASE_FUNCS_URL}/requestTask",
            headers={"accept": "application/json", "Content-Type": "application/json"},
            data=json.dumps(
                {
                    "data": {
                        "text": text,
                        "userId": f"discord_{ctx.user.id}",
                    }
                }
            ),
        )

        if response.status_code == 200:
            result = response.json()["result"]
            task_id = result["taskId"]
            await ctx.respond(f"Task ID is {task_id}")
            return
        else:
            response_json = response.json()
            if "error" in response_json and "message" in response_json["error"]:
                await ctx.respond(f"[ERROR]: {response_json['error']['message']}")
                return
            else:
                await ctx.respond(f"[ERROR]: Unknown ERROR")
                return
    except Exception as error:
        logger.error(f"{error}")
        await ctx.respond(f"[ERROR]: {error}")
        return


bot.run(DISCORD_TOKEN)
