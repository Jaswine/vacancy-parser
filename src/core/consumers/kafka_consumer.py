import json
from aiokafka import AIOKafkaConsumer
import asyncio

from src.core.configs.config import settings


async def consume():
    consumer = AIOKafkaConsumer(
        "account-events",
        bootstrap_servers=settings.KAFKA_BROKERS,
        group_id="verification-group"
    )
    await consumer.start()
    try:
        async for msg in consumer:
            event = json.loads(msg.value)
            if event["type"] == "verification_created":
                send_verification_email.delay(
                    email=event["email"],
                    code=event["code"]
                )
    finally:
        await consumer.stop()

if __name__ == "__main__":
    asyncio.run(consume())
