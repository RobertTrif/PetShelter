Feature: Eliminar gato

  Background:
    Given Exists a worker "worker1_" with password "Hello67_"

  Scenario: Eliminar un gato
    Given I login as worker "worker1_" with password "Hello67_"
    When I click on the "Administracion" button
    Then I should be redirected to the "Administracion" page
    When I select "Gato" from "Eliminar animal"
    Then I should delete de animal "nuevo gato"
    
  Scenario: Eliminar un perro
    Given I login as worker "worker1_" with password "Hello67_"
    When I click on the "Administracion" button
    Then I should be redirected to the "Administracion" page
    When I select "Perro" from "Eliminar animal"
    Then I should delete de animal "rufus"

    Scenario: Eliminar un otro
    Given I login as worker "worker1_" with password "Hello67_"
    When I click on the "Administracion" button
    Then I should be redirected to the "Administracion" page
    When I select "Otro" from "Eliminar animal"
    Then I wait for 16 seconds
    Then I should delete de animal "sebastian"      