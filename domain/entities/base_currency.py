from uuid import uuid4


class Entity:
    """
    Base class for all entities.
    """

    def __init__(self, entity_id: uuid4) -> None:
        self.entity_id = entity_id

    @classmethod
    def generate_uuid(cls) -> uuid4:
        """
        Generates a uuid.
        """
        return uuid4()
