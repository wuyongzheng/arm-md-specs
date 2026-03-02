## B6.3.1 PSCI\_AFFINITY\_INFO command

Query status of a VPE.

This command causes a REC exit due to PSCI. In response, the Host should provide the target REC (identified by target\_affinity ) by calling RMI\_PSCI\_COMPLETE.

## See also:

- A2.3.2 REC attributes
- A4.3.7 REC exit due to PSCI
- B4.3.7 RMI\_PSCI\_COMPLETE command
- B6.3.2 PSCI\_CPU\_OFF command
- B6.3.3 PSCI\_CPU\_ON command

## B6.3.1.1 Interface

## B6.3.1.1.1 Input values

| Name                   | Register   | Bits   | Type   | Description                                                                            |
|------------------------|------------|--------|--------|----------------------------------------------------------------------------------------|
| fid                    | X0         | 63:0   | UInt64 | FID, value 0xC4000004                                                                  |
| target_affinity        | X1         | 63:0   | Bits64 | This parameter contains a copy of the affinity fields of the MPIDR register            |
| lowest_affinity_leve l | X2         | 31:0   | UInt32 | Denotes the lowest affinity level field that is valid in the target_affinity parameter |

The following unused bits of PSCI\_AFFINITY\_INFO input values SBZ: X2[63:32].

## B6.3.1.1.2 Context

The PSCI\_AFFINITY\_INFO command operates on the following context.

| Name       | Type   | Value                          | Before   | Description   |
|------------|--------|--------------------------------|----------|---------------|
| target_rec | RmmRec | RecFromMpidr( target_affinity) | false    | Target REC    |

## B6.3.1.1.3 Output values

| Name   | Register   | Bits   | Type           | Description         |
|--------|------------|--------|----------------|---------------------|
| result | X0         | 63:0   | PsciReturnCode | Command return code |

## B6.3.1.2 Failure conditions

| ID           | Condition                                                               |
|--------------|-------------------------------------------------------------------------|
| target_bound | pre: lowest_affinity_level != 0 post: result == PSCI_INVALID_PARAMETERS |

ID

## Condition

```
target_match pre: !MpidrIsUsed(target_affinity) post: result == PSCI_INVALID_PARAMETERS
```

## B6.3.1.2.1 Failure condition ordering

The PSCI\_AFFINITY\_INFO command does not have any failure condition orderings.

## B6.3.1.3 Success conditions

## Condition

## ID

```
runnable pre: target_rec.flags.runnable == RUNNABLE post: result == PSCI_SUCCESS not_runnable pre: target_rec.flags.runnable == NOT_RUNNABLE post: result == PSCI_OFF
```

## B6.3.1.4 Footprint

The PSCI\_AFFINITY\_INFO command does not have any footprint.