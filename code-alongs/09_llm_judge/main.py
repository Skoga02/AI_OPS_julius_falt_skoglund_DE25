from agents import coach_agent, ClientDeps
import asyncio
import logfire
from dotenv import load_dotenv


load_dotenv()

logfire.configure()
logfire.instrument_system_metrics()
logfire.instrument_pydantic_ai()


async def main(prompt: str, **kwargs):
    result = await coach_agent.run(prompt, **kwargs)
    print(result.output)


if __name__ == "__main__":
    client = ClientDeps(
        name="Bobby",
        goal="Looking for study opportunities and work opportunities within train engineering",
        experience_lvl="intermediate",
        weekly_hours=16,
        current_role="IT supporter",
    )
    asyncio.run(
        main(
            "I want to learn about traibs and how to fix them",
            deps=client,
        ),
    )