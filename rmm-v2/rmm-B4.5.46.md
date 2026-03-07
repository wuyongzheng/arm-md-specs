## B4.5.46 RMI\_REALM\_CREATE command

Creates a Realm.

The RMI\_REALM\_CREATE command may initiate a Stateful RMI Operation.

The RMI\_REALM\_CREATE command may initiate a memory-transferring RMI Operation.

## See also:

- A2.2 Realm
- A2.2.6 Realm parameters
- B4.3.4 Object creation and destruction
- B4.5.47 RMI\_REALM\_DESTROY command
- D1.2.1 Realm creation flow

## B4.5.46.1 Interface

## B4.5.46.1.1 Input values

| Name       | Register   | Bits   | Type    | Description            |
|------------|------------|--------|---------|------------------------|
| fid        | X0         | 63:0   | UInt64  | FID, value 0xC4000158  |
| rd         | X1         | 63:0   | Address | PA of the RD           |
| params_ptr | X2         | 63:0   | Address | PA of Realm parameters |

## B4.5.46.1.2 Context

The RMI\_REALM\_CREATE command operates on the following context.

| Name    | Type           | Value                         | Before   | Description      |
|---------|----------------|-------------------------------|----------|------------------|
| rmm_pre | RmmGlobal      | Rmm()                         | true     | RMMglobal state  |
| rmm     | RmmGlobal      | Rmm()                         | false    | RMMglobal state  |
| params  | RmiRealmParams | RmiRealmParamsAt( params_ptr) | false    | Realm parameters |
| realm   | RmmRealm       | RealmAt(rd)                   | false    | Realm            |


## B4.5.46.1.3 Output values

| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |

## B4.5.46.2 Failure conditions

* pat_valid
  * pre: rmm.dynamic.pat_valid != RMM_TRUE
  * post: result.status == RMI_ERROR_GLOBAL
* params_align
  * pre: !AddrIsRmiGranuleAligned(params_ptr)
  * post: result.status == RMI_ERROR_INPUT
* params_pas
  * pre: !NonSecureAccessPermitted(params_ptr)
  * post: result.status == RMI_ERROR_INPUT
* params_valid
  * pre: !RmiRealmParamsIsValid(params_ptr)
  * post: result.status == RMI_ERROR_INPUT
* params_supp
  * pre: !RealmParamsSupported(params)
  * post: result.status == RMI_ERROR_INPUT
* alias
  * pre: AddrInRange(rd, params.rtt_base, (params.rtt_num_start -1) * rmm.dynamic.rmi_granule_size)
  * post: result.status == RMI_ERROR_INPUT
* rd_align
  * pre: !AddrIsRmiGranuleAligned(rd)
  * post: result.status == RMI_ERROR_INPUT
* rd_bound
  * pre: !PaIsDelegableConventionalFine(rd)
  * post: result.status == RMI_ERROR_INPUT
* rd_state
  * pre: GranuleAt(rd).state != GRAN_DELEGATED
  * post: result.status == RMI_ERROR_INPUT
* rtt_align
  * pre: !AddrIsAligned(params.rtt_base, params.rtt_num_start * rmm.dynamic.rmi_granule_size)
  * post: result.status == RMI_ERROR_INPUT
* rtt_num_level
  * pre: !RttConfigIsValid( params.s2sz, params.rtt_level_start, params.rtt_num_start)
  * post: result.status == RMI_ERROR_INPUT
* rtt_state
  * pre: !RttsStateEqual( params.rtt_base, params.rtt_num_start, GRAN_DELEGATED)
  * post: result.status == RMI_ERROR_INPUT
* ats_plane
  * pre: params.ats_plane > params.
* num_aux_planes
  * post: result.status == RMI_ERROR_INPUT
* vmid
  * pre: !VmidsAvailable(params.num_aux_planes + 1)
  * post: result.status == RMI_ERROR_GLOBAL
* mec_policy
  * pre: !MecidAvailable(params.flags0.mec_policy)
  * post: result.status == RMI_ERROR_GLOBAL

## B4.5.46.2.1 Failure condition ordering

The RMI\_REALM\_CREATE command does not have any failure condition orderings.

## B4.5.46.3 Success conditions

* num_realms
  * post: rmm.dynamic.num_realms == rmm_pre.dynamic.num_realms + 1
* rd_state
  * post: GranuleAt(rd).state == GRAN_RD
* realm_state
  * post: realm.state == REALM_NEW
* rec_index
  * post: realm.rec_index == 0
* rtt_base
  * post: RealmRttBaseEqual( realm, params.rtt_base, params.aux_rtt_base)
* rtt_state
  * post: RttsStateEqual( realm.rtt_base[[0]], realm.rtt_num_start, GRAN_RTT)
* rtte_p_states
  * post: RttsAllProtectedEntriesState( realm.rtt_base[[0]], realm.rtt_num_start, RTTE_VOID)
* rtte_up_states
  * post: RttsAllUnprotectedEntriesState( realm.rtt_base[[0]], realm.rtt_num_start, RTTE_UNMAPPED_NS)
* rtte_ripas
  * post: RttsAllProtectedEntriesRipas( realm.rtt_base[[0]], realm.rtt_num_start, RIPAS_EMPTY)
* lpa2
  * post: Equal(realm.feat_lpa2, params.flags0.lpa2)
* ipa_width
  * post: realm.ipa_width == params.s2sz
* hash_algo
  * post: Equal(realm.hash_algo, params.hash_algo)
* rim
  * post: realm.rim == Zeros{ RMM_REALM_MEASUREMENT_WIDTH}()
* rem
  * post: (realm.rem[[0]] == Zeros{ RMM_REALM_MEASUREMENT_WIDTH}() && realm.rem[[1]] == Zeros{ RMM_REALM_MEASUREMENT_WIDTH}() && realm.rem[[2]] == Zeros{ RMM_REALM_MEASUREMENT_WIDTH}() && realm.rem[[3]] == Zeros{ RMM_REALM_MEASUREMENT_WIDTH}())
* rtt_level
  * post: realm.rtt_level_start == params.rtt_level_start
* rtt_num
  * post: realm.rtt_num_start == params.
* rtt_num_startrpv
  * post: realm.rpv == params.
* rpvda
  * post: Equal(realm.feat_da, params.flags0.da)
* ats
  * post: Equal(realm.feat_ats, params.flags1.ats)
* ats_plane
  * post: realm.ats_plane == params.ats_plane
* rtt_tree_per_plane
  * post: Equal(realm.rtt_tree_per_plane, params.flags1.rtt_tree_per_plane)
* num_aux_planes
  * post: realm.num_aux_planes == params.num_aux_planes
* rtt_s2ap_encoding
  * post: Equal(realm.rtt_s2ap_encoding, params.flags1.rtt_s2ap_encoding)
* lfa_policy
  * post: Equal(realm.lfa_policy, params.flags0.lfa_policy)
* mec_policy
  * post: Equal(realm.mec_policy, params.flags0.mec_policy)
* num_recs
  * post: realm.num_recs == 0
* num_vdevs
  * post: realm.num_vdevs == 0
* num_vsmmus
  * post: realm.num_vsmmus == 0

## B4.5.46.4 RMI\_REALM\_CREATE initialization of RIM

On successful execution of RMI\_REALM\_CREATE, the initial RIM value of the target Realm is zero.

See also:

- A7.1.1 Realm Initial Measurement

## B4.5.46.5 Footprint

| ID        | Value                                                       |
|-----------|-------------------------------------------------------------|
| rd_state  | GranuleAt(rd).state                                         |
| rtt_state | RttsGranuleState( realm.rtt_base[[0]], realm.rtt_num_start) |

<!-- image -->