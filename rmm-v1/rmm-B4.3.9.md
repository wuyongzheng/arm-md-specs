## B4.3.9 RMI\_REALM\_CREATE command

Creates a Realm.

See also:

- A2.1 Realm
- A2.1.6 Realm parameters
- B4.3.10 RMI\_REALM\_DESTROY command
- D1.2.1 Realm creation flow

## B4.3.9.1 Interface

## B4.3.9.1.1 Input values

| Name       | Register   | Bits   | Type    | Description            |
|------------|------------|--------|---------|------------------------|
| fid        | X0         | 63:0   | UInt64  | FID, value 0xC4000158  |
| rd         | X1         | 63:0   | Address | PA of the RD           |
| params_ptr | X2         | 63:0   | Address | PA of Realm parameters |

## B4.3.9.1.2 Context

The RMI\_REALM\_CREATE command operates on the following context.

| Name   | Type           | Value                   | Before   | Description      |
|--------|----------------|-------------------------|----------|------------------|
| params | RmiRealmParams | RealmParams(params_ptr) | false    | Realm parameters |
| realm  | RmmRealm       | Realm(rd)               | false    | Realm            |

## B4.3.9.1.3 Output values

| Name   | Register   | Bits   | Type                 | Description           |
|--------|------------|--------|----------------------|-----------------------|
| result | X0         | 63:0   | RmiCommandReturnCode | Command return status |

## B4.3.9.2 Failure conditions

| ID           | Condition                                                                                   |
|--------------|---------------------------------------------------------------------------------------------|
| params_align | pre: !AddrIsGranuleAligned(params_ptr) post: ResultEqual(result, RMI_ERROR_INPUT)           |
| params_bound | pre: !PaIsDelegable(params_ptr) post: ResultEqual(result, RMI_ERROR_INPUT)                  |
| params_pas   | pre: !GranuleAccessPermitted(params_ptr, PAS_NS) post: ResultEqual(result, RMI_ERROR_INPUT) |
| params_valid | pre: !RmiRealmParamsIsValid(params_ptr) post: ResultEqual(result, RMI_ERROR_INPUT)          |

ID

## Condition

```
params_supp pre: !RealmParamsSupported(params) post: ResultEqual(result, RMI_ERROR_INPUT) alias pre: AddrInRange(rd, params.rtt_base, (params.rtt_num_start -1) * RMM_GRANULE_SIZE) post: ResultEqual(result, RMI_ERROR_INPUT) rd_align pre: !AddrIsGranuleAligned(rd) post: ResultEqual(result, RMI_ERROR_INPUT) rd_bound pre: !PaIsDelegable(rd) post: ResultEqual(result, RMI_ERROR_INPUT) rd_state pre: Granule(rd).state != DELEGATED post: ResultEqual(result, RMI_ERROR_INPUT) rtt_align pre: !AddrIsAligned(params.rtt_base, params.rtt_num_start * RMM_GRANULE_SIZE) post: ResultEqual(result, RMI_ERROR_INPUT) rtt_num_level pre: !RttConfigIsValid( params.s2sz, params.rtt_level_start, params.rtt_num_start) post: ResultEqual(result, RMI_ERROR_INPUT) rtt_state pre: !RttsStateEqual( params.rtt_base, params.rtt_num_start, DELEGATED) post: ResultEqual(result, RMI_ERROR_INPUT) vmid_valid pre: !VmidIsValid(params.vmid) || !VmidIsFree(params.vmid) post: ResultEqual(result, RMI_ERROR_INPUT)
```

## B4.3.9.2.1 Failure condition ordering

The RMI\_REALM\_CREATE command does not have any failure condition orderings.

## B4.3.9.3 Success conditions

| ID             | Condition                                                                                   |
|----------------|---------------------------------------------------------------------------------------------|
| rd_state       | Granule(rd).state == RD                                                                     |
| realm_state    | Realm(rd).state == REALM_NEW                                                                |
| rec_index      | Realm(rd).rec_index == 0                                                                    |
| rtt_base       | Realm(rd).rtt_base == params.rtt_base                                                       |
| rtt_state      | RttsStateEqual( Realm(rd).rtt_base, Realm(rd).rtt_num_start, RTT)                           |
| rtte_p_states  | RttsAllProtectedEntriesState( Realm(rd).rtt_base, Realm(rd).rtt_num_start, UNASSIGNED)      |
| rtte_up_states | RttsAllUnprotectedEntriesState( Realm(rd).rtt_base, Realm(rd).rtt_num_start, UNASSIGNED_NS) |
| rtte_ripas     | RttsAllProtectedEntriesRipas( Realm(rd).rtt_base, Realm(rd).rtt_num_start, EMPTY)           |
| lpa2           | Equal(realm.feat_lpa2, params.flags.lpa2)                                                   |

## ID

## Condition

```
ipa_width Realm(rd).ipa_width == params.s2sz hash_algo Equal(Realm(rd).hash_algo, params.hash_algo) rim Realm(rd).measurements[0] == RimInit( Realm(rd).hash_algo, params) rem (Realm(rd).measurements[1] == Zeros() && Realm(rd).measurements[2] == Zeros() && Realm(rd).measurements[3] == Zeros() && Realm(rd).measurements[4] == Zeros()) rtt_level Realm(rd).rtt_level_start == params.rtt_level_start rtt_num Realm(rd).rtt_num_start == params.rtt_num_start vmid Realm(rd).vmid == params.vmid rpv Realm(rd).rpv == params.rpv num_recs realm.num_recs == 0
```

## B4.3.9.4 RMI\_REALM\_CREATE initialization of RIM

On successful execution of RMI\_REALM\_CREATE, the initial RIM value of the target Realm is calculated by the RMMas follows:

1. Allocate a zero-filled RmiRealmParams data structure to hold the measured Realm parameters.
2. Copy the following attributes from the Host-provided RmiRealmParams data structure into the measured Realm parameters data structure:
- flags
- s2sz
- sve\_vl
- num\_bps
- num\_wps
- pmu\_num\_ctrs
- hash\_algo
3. Using the RHA of the target Realm, compute the hash of the measured Realm parameters data structure. Set the RIM of the target Realm to this value, zero filling upper bytes if the RHA output is smaller than the size of the RIM.

## See also:

- A7.1.1 Realm Initial Measurement
- B3.48 RimInit function
- B4.4.12 RmiRealmParams type

## B4.3.9.5 Footprint

| ID        | Value                                                          |
|-----------|----------------------------------------------------------------|
| rd_state  | Granule(rd).state                                              |
| rtt_state | RttsGranuleState( Realm(rd).rtt_base, Realm(rd).rtt_num_start) |