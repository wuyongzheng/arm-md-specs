## 4.2 Prefetch

Two forms of prefetch command are available which can prefetch the configuration or translation data associated with a stream.

Valid prefetch commands with out of range parameters do not generate command errors. A request to prefetch an address that is out of range with respect to the translation table configuration for the StreamID or SubstreamID is IGNORED and does not record any kind of fault or error.

An implementation is not required to check the range of an Address parameter, but if it does then the parameter is considered out of range if:

- When the stream configuration enables stage 1 translation, the parameter has bits at Address[VAS-1] and upwards that are not all equal in value. TBI is permitted but not required to apply to the parameter.
- When the stream configuration enables stage 2 translation, the parameter has bits at Address[IAS] and upwards that are not zero.

If either SMMU\_IDR1.SSIDSIZE == 0 or STE.S1CDMax == 0, then:

- Prefetch commands must be submitted with SSV == 0 and the SubstreamID parameter is IGNORED.
- Setting SSV == 1 is CONSTRAINED UNPREDICTABLE and has one of the following behaviors:
- -The command behaves as though SSV == 0.
- -The command has no effect.

Prefetch commands directed to invalid configuration, for example, an STE or CD with V == 0 or out of range of the Stream table (or level-2 sub-table), fail silently and do not record error events. Similarly, prefetch commands directed to addresses that cause translation-related faults for any reason do not record error events.

When SMMU\_(*\_)CR0.SMMUEN == 0, valid prefetch commands are consumed but do not trigger a prefetch.

## 4.2.1 CMD\_PREFETCH\_CONFIG(StreamID, SSec, SubstreamID, SSV)

<!-- image -->

Prefetch any STE and CD configuration structures that are required to process traffic from the given StreamID, and SubstreamID if SSV == 1. An implementation is not required to prefetch any, or all, of the configuration requested.

If the STE of a StreamID configures both stage 1 and stage 2 translation, stage 2 HTTU is enabled, and if a CD or L1CD is fetched, then this command sets AF == 1 in the stage 2 translation table descriptor that is used to fetch the CD or L1CD.

Note: The CD might not be fetched if it is already cached.

The common behaviors for SSec apply. See 4.1.6 Common command fields .

## 4.2.2 CMD\_PREFETCH\_ADDR(StreamID, SSec, SubstreamID, SSV, Addr, NS, Size, Stride)

<!-- image -->

Prefetch any STE and CD configuration structures and TLB entries for the given span of addresses as though accessed by transactions associated with StreamID, and SubstreamID if SSV == 1. An implementation is not required to prefetch any, or all, entries requested.

This command performs a prefetch of one or more TLB entries associated with a sequence of addresses given by:

<!-- formula-not-decoded -->

The Stride parameter expresses the expected size of each resulting TLB entry, for the intended span. It controls the gap between successive addresses for which translations are prefetched. This parameter is encoded so that prefetches occur at a stride of 2 12+Stride bytes. For SMMUv3.0 implementations, Stride is RES0, must be set to 0, and the effective prefetch stride is 4KB. Use of a non-zero value either ignores the value or results in a CERROR\_ILL.

The Size parameter expresses the desired number of prefetched translations, made for addresses at the effective Stride size, encoded as a 2 Size multiple of the stride size.

The NS parameter is used in the scenario where the command targets a Secure stream and one of the following applies:

- The stream is configured for stage 2 translation only.
- The stream is configured for stage 1 and stage 2 translation, but stage 1 translation is bypassed.

In these scenarios, the NS parameter is used as the NS attribute required to be input to Secure stage 2 translation. The NS parameter is ignored when stage 2 translation is not performed or when stage 1 translation is performed. Note: When stage 1 translation is performed, the NS attribute provided to stage 2 comes from stage 1 translation tables.

When SMMU\_S\_IDR1.SEL2 == 0, the NS parameter is RES0.

For CMD\_PREFETCH\_ADDR commands issued to the Non-secure Command queue, the NS parameter is RES0. For CMD\_PREFETCH\_ADDR commands issued to the Secure Command queue with SSec == 0, the NS parameter is RES0.

An implementation internally limits the number of translation operations performed so that the overall prefetch operation completes in a reasonable time.

Note: An implementation might achieve this by ceasing prefetch at a point after which further prefetch would overwrite TLB entries prefetched earlier in the same operation.

Note: If translation table entries have been created for a range of addresses with a consistent page or block size, a prefetch operation can be optimized by setting Stride to align with the page or block size of the range.

Note: In some configurations, particularly those with smaller page sizes, it might negatively impact performance to request a prefetch of a span that results in insertion of a large number of TLB entries.

When HTTU is enabled, this command:

- Marks a stage 2 translation table descriptor as accessed for a CD fetch through stage 2 as described in 4.2.1 CMD\_PREFETCH\_CONFIG(StreamID, SSec, SubstreamID, SSV) above.
- Performs HTTU in a manner consistent with that of a speculative read. See sections 3.14 Speculative accesses and 3.13 Translation tables and Access flag/Dirty state .

The common behaviors for SSec apply. See 4.1.6 Common command fields .

When issued to a Realm command queue, CMD\_PREFETCH\_ADDR.NS is RES0 and the address is in Realm address space.