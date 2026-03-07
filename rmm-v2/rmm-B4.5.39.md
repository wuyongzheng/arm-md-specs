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


## B4.5.39.1.3 Output values

| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |

## B4.5.39.2 Failure conditions

* feat
  * pre: Rmm().static.feat_da != FEATURE_TRUE
  * post: result.status == RMI_ERROR_NOT_SUPPORTED
* psmmu_valid
  * pre: !PsmmuAddrIsValid(psmmu_ptr)
  * post: result.status == RMI_ERROR_INPUT
* psmmu_state
  * pre: psmmu.state != PSMMU_INACTIVE
  * post: result.status == RMI_ERROR_INPUT
* params_align
  * pre: !AddrIsRmiGranuleAligned(params_ptr)
  * post: result.status == RMI_ERROR_INPUT
* params_pas
  * pre: !NonSecureAccessPermitted(params_ptr)
  * post: result.status == RMI_ERROR_INPUT
* msi_supp
  * pre: (params.flags.msi == RMI_FEATURE_TRUE && psmmu.feat_msi != FEATURE_TRUE)
* gerror_valid
  * pre: (params.flags.msi == RMI_FEATURE_TRUE && !MsiAddrIsValid(params.gerr_addr))
* eventq_valid
  * pre: (params.flags.msi == RMI_FEATURE_TRUE && !MsiAddrIsValid(params.eventq_addr))
* priq_valid
  * pre: (params.flags.msi == RMI_FEATURE_TRUE && !MsiAddrIsValid(params.priq_addr))
* ats_supp
  * pre: (params.flags.ats == RMI_FEATURE_TRUE && psmmu.feat_ats != FEATURE_TRUE)
* pri_supp
  * pre: (params.flags.pri == RMI_FEATURE_TRUE && psmmu.feat_pri != FEATURE_TRUE)
* dpt
  * pre: (params.flags.ats == RMI_FEATURE_TRUE && DptL0().state != DPT_L0_VALID)

## B4.5.39.3 Success conditions

* state
  * post: psmmu.state == PSMMU_ACTIVE
* gerr_addr
  * post: params.flags.msi == RMI_FEATURE_TRUE psmmu.msi_config.gerr_addr == params.gerr_addr
* gerr_data
  * post: params.flags.msi == RMI_FEATURE_TRUE psmmu.msi_config.gerr_data == params.gerr_data
* eventq_addr
  * post: params.flags.msi == RMI_FEATURE_TRUE psmmu.msi_config.eventq_addr == params.eventq_addr
* eventq_data
  * post: params.flags.msi == RMI_FEATURE_TRUE psmmu.msi_config.eventq_data == params.eventq_data
* priq_addr
  * post: params.flags.msi == RMI_FEATURE_TRUE psmmu.msi_config.priq_addr == params.priq_addr
* priq_data
  * post: params.flags.msi == RMI_FEATURE_TRUE psmmu.msi_config.priq_data == params.priq_data
* params_align
  * pre: !AddrIsRmiGranuleAligned(params_ptr)
  * post: result.status == RMI_ERROR_INPUT
* params_pas
  * pre: !NonSecureAccessPermitted(params_ptr)
  * post: result.status == RMI_ERROR_INPUT
* msi_supp
  * pre: (params.flags.msi == RMI_FEATURE_TRUE && psmmu.feat_msi != FEATURE_TRUE)
  * post: result.status == RMI_ERROR_INPUT
* gerror_valid
  * pre: (params.flags.msi == RMI_FEATURE_TRUE && !MsiAddrIsValid(params.gerr_addr))
  * post: result.status == RMI_ERROR_INPUT
* eventq_valid
  * pre: (params.flags.msi == RMI_FEATURE_TRUE && !MsiAddrIsValid(params.eventq_addr))
  * post: result.status == RMI_ERROR_INPUT
* priq_valid
  * pre: (params.flags.msi == RMI_FEATURE_TRUE && !MsiAddrIsValid(params.priq_addr))
  * post: result.status == RMI_ERROR_INPUT
* ats_supp
  * pre: (params.flags.ats == RMI_FEATURE_TRUE && psmmu.feat_ats != FEATURE_TRUE)
  * post: result.status == RMI_ERROR_INPUT
* pri_supp
  * pre: (params.flags.pri == RMI_FEATURE_TRUE && psmmu.feat_pri != FEATURE_TRUE)
  * post: result.status == RMI_ERROR_INPUT
* dpt
  * pre: (params.flags.ats == RMI_FEATURE_TRUE && DptL0().state != DPT_L0_VALID)
  * post: result.status == RMI_ERROR_DEVICE B4.5.39.2.1 Failure condition ordering The RMI_PSMMU_ACTIVATE command does not have any failure condition orderings. Chapter B4. Realm Management Interface B4.5. RMI commands

## B4.5.39.4 Footprint

The RMI\_PSMMU\_ACTIVATE command does not have any footprint.

<!-- image -->