## 3.26 Permission Indirections

The Armv8.9 architecture[2] introduces a permissions indirection scheme, for stage 1 and stage 2 independently. This section describes the corresponding SMMU architecture changes for this feature.

## 3.26.1 Stage 1 permission indirections

Note: PIIndex is a translation table descriptor field, introduced by FEAT\_S1POE in the A-profile architecture[2].

Stage 1 permissions are determined according to feature support and control bits as follows:

|   SMMU_IDR3.S1PI | STE.S1PIE   | CD.PIE   | Result                                                                                                                             |
|------------------|-------------|----------|------------------------------------------------------------------------------------------------------------------------------------|
|                0 | RES0        | RES0     | Stage 1 permission indirections are not supported and stage 1 permissions are determined directly from stage 1 translation tables. |
|                1 | 0           | RES0     | Stage 1 permissions are determined directly from stage 1 translation tables.                                                       |
|                1 | 1           | 0        | Stage 1 permissions are determined directly from stage 1 translation tables.                                                       |
|                1 | 1           | 1        | Stage 1 permissions are determined from CD.PIIP, and CD.PIIU if appropriate, using PIIndex from the stage 1 descriptors.           |

Note: The STE.S1PIE control allows a hypervisor to prevent stage 1 configuration of permission indirections, for StreamIDs where Context Descriptors are controlled directly by a guest. In this case, the hypervisor is expected to present an emulated SMMU without support for permission indirections to the guest.

Note: The SMMU does not support the stage 1 permission overlay feature present in the PE architecture.

If the stage 1 Indirect Permission Scheme is enabled, then CD.WXN is RES0 and has no effect.

If the stage 1 Indirect Permission Scheme is enabled, the stage 1 permissions are computed as follows:

1. The permissions are decoded from CD.PIIU[PIIndex] and CD.PIIP[PIIndex].
2. For the NS-EL1, Secure, Realm-EL1 and any-EL2-E2H StreamWorlds, CD.PAN is applied as follows:
- If CD.PAN is 1 and any Unprivileged access is granted then Privileged read and write permissions are removed. This applies regardless of the value of CD.EPAN.
- It is IMPLEMENTATION DEFINED whether this step is performed here or after step 4.
3. For a translation for Secure state, then if SMMU\_S\_CR0.SIF is 1 and the stage 1 output address is Non-secure, then both Privileged execute and Unprivileged execute permission are removed.
4. For a translation for Realm state, then if the stage 1 output address is Non-secure, then both Privileged execute and Unprivileged execute permission are removed. This permissions computation is not affected by CD.{EPD0, EPD1, E0PD0, E0PD1}.

## 3.26.2 Stage 2 permission indirections

Note: POIndex is a translation table descriptor field, introduced by FEAT\_S2POE in the A-profile architecture[2].

Stage 2 permissions are determined according to feature support and control bits as follows:

|   SMMU_IDR3.S2PI | STE.S2PIE   | STE.S2POE   | Result                                                                                                                                                             |
|------------------|-------------|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                0 | RES0        | RES0        | Stage 2 permission indirections are not supported and stage 2 permissions are determined directly from stage 2 translation tables.                                 |
|                1 | 0           | 0           | Stage 2 permissions are determined directly from stage 2 translation tables.                                                                                       |
|                1 | 0           | 1           | ILLEGAL, generates C_BAD_STE.                                                                                                                                      |
|                1 | 1           | 0           | Stage 2 permissions are determined from SMMU_S2PII using PIIndex from the stage 2 descriptors.                                                                     |
|                1 | 1           | 1           | Stage 2 permissions are determined from STE.S2POI using POIndex from the stage 2 descriptors, combined with SMMU_S2PII using PIIndex from the stage 2 descriptors. |

Stage 2 permissions are computed in the following order, and F\_PERMISSION events are reported with this priority from highest to lowest:

1. For the stage 2 translation of a stage 1 output address, including next-level table addresses of a stage 1 translation table walk, the AssuredOnly permission check is applied.
2. The Base and Overlay permissions are applied as follows:
- If permission overlays are enabled, the Overlay permissions are looked up from STE.S2POI indexed by POIndex.
- If permission indirection is enabled then the Base permissions are looked up from SMMU\_S2PII indexed by PIIndex. Otherwise, the Base permissions are taken directly from the translation table descriptor.
- The base and overlay permissions are combined as described in the A-profile architecture[2] and the resulting permissions are applied.
3. For the translation of a stage 1 translation table walk or CD fetch, the effect of STE.S2PTW is applied.
4. For any access that requires write permission, if permission indirection is enabled, the Dirty state permission check is applied.
5. For directed prefetch operations and cache maintenance operations, the effects of STE.DRE and STE.DCP are applied.