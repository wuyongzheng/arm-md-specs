## 5.6 VMS, Virtual Machine Structure

The VMS characteristics are:

Structure for per-VM configuration that can be shared across multiple StreamIDs with the same S2VMID.

VMS is a 4096-byte structure.

## Field descriptions

The Virtual Machine Structure, VMS, is an SMMU concept and is a structure that is located from the pointer field STE.VMSPtr. The VMS holds per-VM facilities. The VMS is 4KB in size and is 4KB-aligned.

Multiple STEs can point to the same VMS if required, for example to avoid duplication.

If a group of STEs with the same VMID contain different VMS pointers then it is UNPREDICTABLE which of the pointers are used for VMS access for a given STE in the group.

Note: This means that multiple STEs within a Security state with the same VMID must point to the same VMS.

The VMS is fetched using the same Security state as the STE that references it. The attributes used to access the VMS are the same as those used to fetch STEs in the corresponding Security state. See SMMU\_CR1 and SMMU\_STRTAB\_BASE.

## PARTID\_MAP, bits [511:0]

Map from virtual CD.PARTID values to physical PARTID values.

Array of 32 16-bit little-endian physical PARTIDs, indexed by the virtual PARTID from CD.PARTID for a CD located through the same STE as that of the VMS.

If an entry is configured with a value that is greater than the supported PARTID size, indicated by the corresponding SMMU\_(*\_)MPAMIDR.PARTID\_MAX, an UNKNOWN PARTID is used.

The corresponding SMMU\_(*\_)MPAMIDR.PARTID\_MAX is chosen as follows:

- For a Non-secure Stream, then SMMU\_MPAMIDR.PARTID\_MAX.
- For a Secure Stream, if SMMU\_S\_MPAMIDR.HAS\_MPAM\_NS == 0 or STE.MPAM\_NS == 0, then SMMU\_S\_MPAMIDR.PARTID\_MAX.
- For a Secure Stream, if SMMU\_S\_MPAMIDR.HAS\_MPAM\_NS == 1 and STE.MPAM\_NS == 1, then SMMU\_MPAMIDR.PARTID\_MAX.

Note: There is no equivalent mapping for PMGs because they do not need to be mapped from virtual to physical values.

Note: The number 32 derives from the MPAM PE limit in the A-profile architecture[2].

## Bits [32767:512]

Reserved, RES0.

The area of the VMS outside of the PARTID\_MAP structure is RES0.

Note: It is the intention to use the VMS to extend the SMMU with future per-VM functionality unrelated to MPAM.

## Purpose

## Attributes

## 5.6.1 VMS presence and fetching

The VMS is supported by a Security state if all the statements below are true:

- SMMU\_IDR3.MPAM == 1
- SMMU\_IDR0.S1P == 1
- SMMU\_IDR0.S2P == 1
- For Non-secure state:
- -SMMU\_MPAMIDR.PARTID\_MAX != 0
- For Secure state:
- -SMMU\_S\_IDR1.SEL2 == 1 and any of the following is true:
* SMMU\_S\_MPAMIDR.PARTID\_MAX != 0
* SMMU\_MPAMIDR.PARTID\_MAX != 0 and SMMU\_S\_MPAMIDR.HAS\_MPAM\_NS == 1
- For Realm state, any of the following is true:
- -SMMU\_R\_MPAMIDR.PARTID\_MAX != 0
- -SMMU\_MPAMIDR.PARTID\_MAX != 0 and SMMU\_R\_MPAMIDR.HAS\_MPAM\_NS == 1

The VMS is not always enabled even if an implementation supports it. See STE.VMSPtr for information on when the VMS is enabled.

If the VMS is enabled, an SMMU is permitted but not required to access the VMS when processing a transaction that uses an STE but does not require information from the VMS indicated from the STE. If this happens and the access results in an External abort, the transaction is treated as though it required the VMS and the abort is reported for the transaction as an F\_VMS\_FETCH event.

Note: For example, a nested configuration with STE.S1MPAM == 1 enables the VMS and the VMS is required for a transaction that undergoes both stages of translation. A different transaction using the same STE might bypass stage 1 due to STE.S1DSS == 0b01 configuration and in this case the VMS is permitted to be accessed. This means that VMS access error might be detected and reported relating to a transaction that does not require information from the VMS. See section 7.3.20 F\_VMS\_FETCH .

Note: It is also possible that non-client transaction accesses experience a VMS access error. See section 8.1 PRI queue overflow .

## 5.6.2 VMS caching and invalidation

The contents of VMS.PARTID\_MAP are permitted to be cached as part of any of the following architecturally-visible structures:

- A configuration cache entry.
- -Indexed by StreamID.
- -Invalidated by an operation affecting a StreamID, meaning an invalidation scope of CMD\_CFGI\_STE or wider.
- A separate configuration cache for PARTID\_MAP contents.
- -Indexed by VMID.

PARTID\_MAP information is not cached in a TLB.

Because the PARTID\_MAP contents might be cached in structures indexed by StreamID and VMID, a change to PARTID\_MAP requires invalidation by both StreamID and VMID.

The configuration invalidation commands CMD\_CFGI\_STE and CMD\_CFGI\_STE\_RANGE invalidate cached information that is cached indexed by StreamID from all VMS fields relating to the StreamIDs in the scope of a given command.

The configuration invalidation command CMD\_CFGI\_ALL invalidates cached information regardless of whether it is cached indexed by StreamID or VMID.

The command CMD\_CFGI\_VMS\_PIDM invalidates any separate caching of PARTID\_MAP.

See section 4.3.5.1 Usage for more information on invalidation of VMS fields.

The VMS does not interact with SMMU\_(*\_)CR0.VMW. If STEs with different VMIDs point to a common VMS, information from the VMS might be cached multiple times and invalidation will require multiple operations that apply to all VMIDs that reference the VMS.