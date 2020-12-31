class Bot:
    def __init__(self, json_data: dict):
        self.json_data = json_data[0]

    @property
    def id(self) -> int:
        return self.json_data['id']

    @property
    def botID(self) -> int:
        return self.json_data['botID']

    @property
    def prefix(self) -> str:
        return self.json_data['prefix']

    @property
    def ownerID(self) -> str:
        return self.json_data['ownerID']

    @property
    def shortDesc(self) -> str:
        return self.json_data['shortDesc']

    @property
    def longDesc(self) -> str:
        return self.json_data['longDesc']

    @property
    def botServer(self) -> str:
        invite_id = self.json_data['botServer']
        return f'https://discord.gg/{invite_id}'

    @property
    def botWebsite(self) -> str:
        return self.json_data['botWebsite']

    @property
    def customInvite(self) -> str:
        return self.json_data['customInvite']

    @property
    def botTags(self) -> list:
        return self.json_data['botTags']

    @property
    def inTesting(self) -> bool:
        return self.json_data['inTesting']

    @property
    def isApproved(self) -> bool:
        return self.json_data['isApproved']

    @property
    def inMain(self) -> bool:
        return self.json_data['inMain']

    @property
    def testedBy(self) -> int:
        return self.json_data['testedBy']

    @property
    def submittedOn(self) -> int:
        return self.json_data['submittedOn']

    @property
    def approvedOn(self) -> int:
        return self.json_data['approvedOn']

    @property
    def totalUpvotes(self) -> int:
        return self.json_data['totalUpvotes']

    @property
    def guildsCount(self) -> int:
        return self.json_data['guildsCount']

    @property
    def verifiedBot(self) -> bool:
        return self.json_data['verifiedBot']

    @property
    def createdAt(self) -> bool:
        return self.json_data['createdAt']

    @property
    def updatedAt(self) -> bool:
        return self.json_data['updatedAt']
