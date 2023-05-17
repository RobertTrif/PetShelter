Feature: Create instances
    workers will have to be able to create new instances
    
    Background: There is a registered worker
        Given Exists a worker "worker1_" with password "Hello67_"

    Scenario: Create a cat
        Given I login as worker "worker1_" with password "Hello67_"
