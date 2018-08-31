@service @jyver @registration
Feature: Onboarding Registration API
  In order to display relevant messages to an applicant during registration,
  As an application developer for Jyve
  I want to get relevant registration information via a REST API

  Scenario Outline: Invalid ZIP Code API Check
    When the Registration API is queried with
      | zipcode   | expected_result   |
      | <zipcode> | <expected_result> |
    Then the API returns a result of <expected_result>

    Examples: Not Real ZIP Code
      | zipcode  | expected_result |
      | 22222    | False           |
      | 33333    | False           |
      
    Examples: Real ZIP Code
      | zipcode  | expected_result |
      | 94103    | True           |
      | 34241    | True           |
   

