from service import Service


class GuruTaxi(Service):
    async def run(self):
        await self.client.post("https://guru.taxi/api/v1/driver/session/verify",
                               json={"phone": {"code": 1, "number": self.phone}})
