# components.py
from abc import ABC, abstractmethod

class BaseComponent(ABC):
    @abstractmethod
    def process(self, data):
        pass

class DataValidationComponent(BaseComponent):
    def process(self, data):
        # Implement data validation logic
        return validated_data

class DataTransformationComponent(BaseComponent):
    def process(self, data):
        # Implement data transformation logic
        return transformed_data

class DataPersistenceComponent(BaseComponent):
    def __init__(self, db_session):
        self.db_session = db_session

    def process(self, data):
        # Implement data persistence logic
        self.db_session.add(data)
        self.db_session.commit()
        return data

# Usage example
def process_data_pipeline(data, db):
    validation_component = DataValidationComponent()
    transformation_component = DataTransformationComponent()
    persistence_component = DataPersistenceComponent(db)

    validated_data = validation_component.process(data)
    transformed_data = transformation_component.process(validated_data)
    persisted_data = persistence_component.process(transformed_data)

    return persisted_data
