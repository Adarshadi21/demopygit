Feature: SagePub Automation

  Scenario: Navigate through SagePub website
    Given I access "https://sk.sagepub.com/"
    When I click on the "Academic Books" title
    And I click on 13 titles under "Browser By >> Discipline"
    Then I print the unique integer along with the clicked title name