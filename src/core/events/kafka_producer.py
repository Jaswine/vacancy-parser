from aiokafka import AIOKafkaProducer
import json
import asyncio

from src.core.configs.config import settings

producer = None

async def init_kafka():
    global producer
    producer = AIOKafkaProducer(
        bootstrap_servers=settings.KAFKA_BROKERS
    )
    await producer.start()

async def publish_verification_event(account_id: int, email: str, code: str):
    global producer
    await producer.send_and_wait(
        "account-events",
        json.dumps({
            "type": "verification_created",
            "account_id": account_id,
            "email": email,
            "code": code
        }).encode("utf-8")
    )
