## Chapter 13

## Attribute Transformation

The Arm architecture supports a set of attributes that accompanies each external access that is made by a PE. These attributes map onto attributes carried by the interconnect in an interconnect-specific manner. The SMMU supports a set of attributes that is identical to that supported by the PE. These attributes govern the behavior of each client transaction and are presented from the SMMU to the memory system. The interconnect from the client device might also present attributes to the SMMU. This section describes how the attributes output with a transaction are determined from the SMMU configuration and the attributes supplied with the transaction on input.

To avoid interconnect-specific language, this section uses attribute terminology and concepts as defined in the Arm Architecture Reference Manual [2]. The mapping of these attributes onto interconnect implementations that support a subset of the attributes is IMPLEMENTATION DEFINED.

This section covers the attributes that are applied in the four conditions under which a transaction can pass through an SMMU:

1. Global bypass. The SMMU is disabled (SMMU\_(S\_)CR0.SMMUEN == 0).
2. STE bypass. The SMMU is enabled but all stages of translation are disabled by an STE.
3. Normal translation flow. An STE configures one or more stages of translation.
4. PCIe ATS Translated. A device requests a 'pre-translation', caches the result, and subsequently presents a transaction with an address that has been translated but has not had SMMU attributes applied.

This section additionally covers accesses that originate from the SMMU, such as fetching configuration or walking translation tables.

Depending on the path taken, attributes might be overridden or modified by SMMU configuration registers, STE fields or translation table entries. Some of the attributes are used when checking access permissions in translation table entries, others are provided for the memory system.

At the highest level, the attribute determination for the normal translation flow is:

1. Input attributes are obtained from the incoming transaction and any attributes that are not provided are generated from constant default values.
2. The STE might then override incoming attributes for a specific stream.
3. The stage 1 and stage 2 translation table permissions are checked against the attributes determined from the previous step, where a stage is enabled.
4. If stage 1 is enabled, the stage 1 translation table attributes replace any input and STE override values.
5. If stage 2 is enabled, the stage 2 translation table attributes are combined with the stage 1 attributes if stage 1 is enabled, or combined with the overridden input attributes if stage 1 is not enabled.
6. The attribute is output with the translated transaction.