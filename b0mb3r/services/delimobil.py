from service import Service


class DeliMobil(Service):
    async def run(self):
        await self.client.post("https://api.delitime.ru/api/v2/signup",
                               data={"SignupForm[username]": self.formatted_phone, "SignupForm[device_type]": 3})
