## B4.5.39 RMI\_PSMMU\_ACTIVATE command

Activate a PSMMU.

The RMI\_PSMMU\_ACTIVATE command may initiate a Stateful RMI Operation.

The RMI\_PSMMU\_ACTIVATE command may initiate a memory-transferring RMI Operation.

## See also:

- A9.7 Physical SMMU
- A9.7.6 PSMMU interrupts
- B4.5.40 RMI\_PSMMU\_DEACTIVATE command

## B4.5.39.1 Interface

## B4.5.39.1.1 Input values

| Name       | Register   | Bits   | Type    | Description            |
|------------|------------|--------|---------|------------------------|
| fid        | X0         | 63:0   | UInt64  | FID, value 0xC40001D7  |
| psmmu_ptr  | X1         | 63:0   | Address | PA of PSMMU            |
| params_ptr | X2         | 63:0   | Address | PA of PSMMU parameters |

## B4.5.39.1.2 Context

The RMI\_PSMMU\_ACTIVATE command operates on the following context.

| Name   | Type           | Value                         | Before   | Description      |
|--------|----------------|-------------------------------|----------|------------------|
| psmmu  | RmmPsmmu       | PsmmuAt(psmmu_ptr)            | false    | PSMMU            |
| params | RmiPsmmuParams | RmiPsmmuParamsAt( params_ptr) | false    | PSMMU parameters |

DRAFT

## B4.5.39.1.3 Output values

| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |

## B4.5.39.2 Failure conditions

| ID          | Condition                                                                                |
|-------------|------------------------------------------------------------------------------------------|
| feat        | pre: Rmm().static.feat_da != FEATURE_TRUE post: result.status == RMI_ERROR_NOT_SUPPORTED |
| psmmu_valid | pre: !PsmmuAddrIsValid(psmmu_ptr) post: result.status == RMI_ERROR_INPUT                 |
| psmmu_state | pre: psmmu.state != PSMMU_INACTIVE post: result.status == RMI_ERROR_INPUT                |

## ID

## Condition

| params_align   | pre: post:   | !AddrIsRmiGranuleAligned(params_ptr) result.status == RMI_ERROR_INPUT         |
|----------------|--------------|-------------------------------------------------------------------------------|
| params_pas     | pre: post:   | !NonSecureAccessPermitted(params_ptr) result.status == RMI_ERROR_INPUT        |
| msi_supp       | pre:         | (params.flags.msi == RMI_FEATURE_TRUE && psmmu.feat_msi != FEATURE_TRUE)      |
|                | post:        | result.status == RMI_ERROR_INPUT                                              |
| gerror_valid   | pre:         | (params.flags.msi == RMI_FEATURE_TRUE && !MsiAddrIsValid(params.gerr_addr))   |
|                | post:        | result.status == RMI_ERROR_INPUT                                              |
| eventq_valid   | pre:         | (params.flags.msi == RMI_FEATURE_TRUE && !MsiAddrIsValid(params.eventq_addr)) |
|                | post:        | result.status == RMI_ERROR_INPUT                                              |
| priq_valid     | pre:         | (params.flags.msi == RMI_FEATURE_TRUE && !MsiAddrIsValid(params.priq_addr))   |
|                | post:        | result.status == RMI_ERROR_INPUT                                              |
| ats_supp       | pre:         | (params.flags.ats == RMI_FEATURE_TRUE && psmmu.feat_ats != FEATURE_TRUE)      |
|                | post:        | result.status == RMI_ERROR_INPUT                                              |
| pri_supp       | pre:         | (params.flags.pri == RMI_FEATURE_TRUE && psmmu.feat_pri != FEATURE_TRUE)      |
|                | post:        | result.status == RMI_ERROR_INPUT                                              |
| dpt            | pre:         | (params.flags.ats == RMI_FEATURE_TRUE && DptL0().state != DPT_L0_VALID)       |
|                | post:        | result.status == RMI_ERROR_DEVICE                                             |

## B4.5.39.3 Success conditions

DRAFT params\_align pre: !AddrIsRmiGranuleAligned(params\_ptr) post: result.status == RMI\_ERROR\_INPUT params\_pas pre: !NonSecureAccessPermitted(params\_ptr) post: result.status == RMI\_ERROR\_INPUT msi\_supp pre: (params.flags.msi == RMI\_FEATURE\_TRUE &amp;&amp; psmmu.feat\_msi != FEATURE\_TRUE) post: result.status == RMI\_ERROR\_INPUT gerror\_valid pre: (params.flags.msi == RMI\_FEATURE\_TRUE &amp;&amp; !MsiAddrIsValid(params.gerr\_addr)) post: result.status == RMI\_ERROR\_INPUT eventq\_valid pre: (params.flags.msi == RMI\_FEATURE\_TRUE &amp;&amp; !MsiAddrIsValid(params.eventq\_addr)) post: result.status == RMI\_ERROR\_INPUT priq\_valid pre: (params.flags.msi == RMI\_FEATURE\_TRUE &amp;&amp; !MsiAddrIsValid(params.priq\_addr)) post: result.status == RMI\_ERROR\_INPUT ats\_supp pre: (params.flags.ats == RMI\_FEATURE\_TRUE &amp;&amp; psmmu.feat\_ats != FEATURE\_TRUE) post: result.status == RMI\_ERROR\_INPUT pri\_supp pre: (params.flags.pri == RMI\_FEATURE\_TRUE &amp;&amp; psmmu.feat\_pri != FEATURE\_TRUE) post: result.status == RMI\_ERROR\_INPUT dpt pre: (params.flags.ats == RMI\_FEATURE\_TRUE &amp;&amp; DptL0().state != DPT\_L0\_VALID) post: result.status == RMI\_ERROR\_DEVICE B4.5.39.2.1 Failure condition ordering The RMI\_PSMMU\_ACTIVATE command does not have any failure condition orderings.

ID

## Condition

| state       | post:      | psmmu.state == PSMMU_ACTIVE                                                             |
|-------------|------------|-----------------------------------------------------------------------------------------|
| gerr_addr   | pre: post: | params.flags.msi == RMI_FEATURE_TRUE psmmu.msi_config.gerr_addr == params.gerr_addr     |
| gerr_data   | pre: post: | params.flags.msi == RMI_FEATURE_TRUE psmmu.msi_config.gerr_data == params.gerr_data     |
| eventq_addr | pre: post: | params.flags.msi == RMI_FEATURE_TRUE psmmu.msi_config.eventq_addr == params.eventq_addr |
| eventq_data | pre: post: | params.flags.msi == RMI_FEATURE_TRUE psmmu.msi_config.eventq_data == params.eventq_data |
| priq_addr   | pre: post: | params.flags.msi == RMI_FEATURE_TRUE psmmu.msi_config.priq_addr == params.priq_addr     |
| priq_data   | pre: post: | params.flags.msi == RMI_FEATURE_TRUE psmmu.msi_config.priq_data == params.priq_data     |

Chapter B4. Realm Management Interface B4.5. RMI commands

## B4.5.39.4 Footprint

The RMI\_PSMMU\_ACTIVATE command does not have any footprint.

<!-- image -->