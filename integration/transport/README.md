# Integration: Transport

# Run

Run the following command in the root directory of the project:
`$ python3 -m integration.transport.transport`

# Test

Run the following command in the root directory of the project:
`$ python3 -m unittest integration.transport.tests`

# Learnings

## 1. TAM - Is the TAM a function of the scenario?

Yes, for transportation it is. There is a baseline that defines the initial modeshare. For the different scenarios the TAM can change.

## 2. How to model the prioritization of the solutions in the integration scenario

This is about the overallocation.
Best would be a possibility to react to this when it happens.

## 3. Why do the individual solutions provide data in million km and billion km?

This is a know problem. It needs to be solved on integration layer

# Open Questions

## What unit to use?

Billion pass km or passenger-km?
