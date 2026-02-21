## Chapter 18

## Support for Memory Encryption Contexts

The Memory Encryption Contexts feature, FEAT\_MEC, provides finer-grained memory encryption contexts, within the Realm physical address space, to be assigned to Realms, with policy controlled by Realm EL2 [2].

This section introduces a comparable feature for the SMMU architecture for interoperability with the MEC PE extension. This is only applicable for an SMMU with RME DA.

In the SMMU, support for Memory Encryption Contexts (MEC), is indicated in SMMU\_R\_IDR3.MEC.

If the MEC feature is supported, the supported MECID width is indicated in SMMU\_R\_MECIDR.

SMMU- and client-originated accesses to memory are associated with a MECID, that identifies the Memory Encryption Context of the access.

Accesses made by the SMMU or client devices for Secure, Non-secure, and Root PA spaces are issued with the default MECID of zero.

Accesses made by the SMMU or client devices to Realm PA space are associated with a MECID. The choice of MECID depends on the type of access, as described in the descriptions of SMMU\_R\_GMECID and STE.MECID.

Accesses made by NoStreamID client devices to Realm PA space are associated with a MECID provided by the NoStreamID device in an IMPLEMENTATION DEFINED manner.

If an SMMU without the Realm programming interface is integrated in a system that supports MEC, all client- and SMMU-originated accesses for that SMMU are treated as having the default MECID of zero.

Note: This revision of the SMMU architecture does not support Alternative MECID values and use of a descriptor with the AMEC bit set to 1 causes F\_TRANSLATION.

Note: The MEC feature introduces a translation table descriptor bit, AMEC, in both:

- Bit[63] in stage 2 Page and Block descriptors for the Realm EL1&amp;0 translation regime.
- Bit[63] in stage 1 Page and Block descriptors for the Realm EL2 and EL2&amp;0 translation regimes.

If SMMU\_R\_IDR3.MEC == 1 and a Realm translation requires use of a descriptor with the AMEC field set to 1, it is treated as F\_TRANSLATION at the stage of translation that had AMEC set to 1.

Note: For both descriptor formats, the AMEC field is RES0 and treated as 0 if the NS field in the descriptor is 1. In this case it does not trigger F\_TRANSLATION.

If SMMU\_R\_IDR3.MEC == 0, the AMEC field is RES0 and does not trigger F\_TRANSLATION.