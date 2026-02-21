## 3.27 Translation Hardening

## 3.27.1 Protected attribute

If SMMU\_IDR3.THE == 1, SMMU behavior for the stage 1 Protected attribute is the same as for the PE behavior for the Protected attribute, including:

- The Protected attribute is always present in VMSAv9-128 descriptors.
- The Protected attribute is only present in VMSAv8-64 descriptors if CD.PnCH is 1.
- The Contiguous bit is not present in VMSAv8-64 descriptors if CD.PnCH is 1.

Note: The SMMU does not support Read-Check-Write (RCW) operations, and therefore none of the RCW checks are applied by the SMMU.

Note: Unless the STE.AssuredOnly check is enabled, there is no benefit to enabling CD.PnCH in the SMMU, except when VMSAv8-64 stage 1 translation tables for a PE context using the Protected attribute are shared with SMMU contexts, and the SMMU must therefore not interpret bit 52 of Block and Page descriptors as the Contiguous bit.

## 3.27.2 AssuredOnly permission checks

If SMMU\_IDR3.THE == 1, SMMU behavior for the stage 2 AssuredOnly attribute is the same as for the PE behavior for the AssuredOnly attribute, except that:

- Use of the AssuredOnly attribute is configured via STE.AssuredOnly instead of VTCR\_EL2.AssuredOnly.
- A stage 2 Permission fault that would be reported with ESR\_EL2.AssuredOnly set to 1 is instead reported as a stage 2 F\_PERMISSION with AssuredOnly set to 1.
- If a CD, or the L1CD that points to it, is fetched from memory that is not marked AssuredOnly at stage 2, then any access translated from the TTB0 or TTB1 field in that CD does not have the Assured Translation property, and this overrides the Assured Translation property as-defined in the A-profile architecture[2].
- If a CD, and the L1CD that points to it, is fetched from memory that is marked AssuredOnly at stage 2, then any access translated from the TTB0 or TTB1 field in that CD gets the Assured Translation property according to the definition in the A-profile architecture[2].

Note: In the PE architecture, if stage 1 translation is disabled then any access to a region marked AssuredOnly at stage 2 generates a Permission fault. This also applies in the SMMU architecture for any case where stage 1 translation is bypassed, whether because of STE.Config or STE.S1DSS configuration.

For an ATS Translation Request, the AssuredOnly check is performed in the same manner as for a regular transaction, and if the AssuredOnly check fails then the ATS Translation Completion is sent with Success and R == W == 0.

For an ATS Translated Transaction when STE.EATS is 0b10 (Split-stage ATS), then AssuredOnly is ignored for the purposes of determining whether the transaction is permitted.