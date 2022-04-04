from services.ExampleService import ExampleService
from services.RequestService import RequestService



if __name__ == "__main__":
    # Main logic goes here
    
    print(ExampleService.get_example())

    myRequestService = RequestService()

    print(myRequestService.get_example())

