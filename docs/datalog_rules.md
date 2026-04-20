# Datalog Rules

## Dataset Files

### `AgencyFile`

1. A `Dataset` is a `Violation` if it has more than one AgencyFile`.
2. An `AgencyFile` must have at least one `Agency`.
3. An `AgencyFile` is an `AgencyFileWithMultipleAgencies` if it has more than one `Agency`.
4. An `AgencyFile` is an `AgencyFileWithSingleAgency` if it has more than one `Agency`.

## Agencies

1. `agency_id`

   1. The `Agency`