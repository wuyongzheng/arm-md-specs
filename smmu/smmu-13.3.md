## 13.3 Translation flow, STE bypasses stage 1 and stage 2

A second type of SMMU bypass is available when the SMMU is enabled. This is when a StreamID selects an STE configured to bypass (STE.Config == 0b100 ). SMMU\_GBPA and SMMU\_S\_GBPA are not used, and a finer-grained per-STE configuration is available. Refer to the no-translate case of Figure 13.3.

The STE fields MTCFG, MemAttr, ALLOCCFG, SHCFG, NSCFG, PRIVCFG and INSTCFG can override any attribute before the transaction is passed to the memory system. This provides per-StreamID granularity of attribute settings.

Each attribute might take a set value or select to Use incoming. Where the incoming attribute is use, the attribute is either taken from the incoming interconnect or, when not supplied, the default input attribute constructed in the SMMU.

## Pseudocode:

```
// See 13.1.3: Attrs input_attrs = add_defaults_for_unsupplied(upstream_attrs); STE ste = get_STE_for_stream(StreamID); output_attrs = replace_attrs(ste, input_attrs); if (!ste.fetched_for_secure_stream()) { output_attrs.NS = 1; } // MT, SH, RA, WA, TR, INST, PRIV are unchanged or overridden, // depending on respective STE field. // // NS is unchanged or overridden if secure stream, otherwise // fixed at 1. output_attrs = ensure_consistent_attrs(output_attrs);
```