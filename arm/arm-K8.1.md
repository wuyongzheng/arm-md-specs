## K8.1 AArch64 Address translation examples

The VMSAv8 address translation stages that are controlled by an Exception level that is using AArch64 are described in Relationship between translation regimes and implemented Exception levels. Address translation describes the VMSAv8-64 address translation scheme. This section gives examples of the use of that scheme, for common translation requirements.

System registers relevant to MMU operation specifies the relevant registers, including the TCR\_ELx and TTBR\_ELx, or TTBR\_ELx, for each stage of address translation.

For any stage of translation, a TCR\_ELx.T n SZ field indicates the supported input address size. For a stage of address translation controlled from an Exception level using AArch64, the supported input address size is 2 (64-T n SZ) .

This section describes:

- Performing the initial lookup, for an address for which the initial lookup is either:
- -At the highest lookup level used for the appropriate translation granule size.
- -Because of the concatenation of translation tables at the initial lookup level, one level down from the highest level used for the translation granule size.

These descriptions take account of the following cases:

- -The IA size is smaller than the largest size for the translation level, see Input address size configuration.
- -For a stage 2 translation, translation tables are concatenated, to move the initial lookup level down by one level, see Concatenated translation tables.

For examples of performing the initial lookup, see Examples of performing the initial lookup.

- The full translation flow for resolving a page of memory. These examples describe resolving the largest IA size supported by the initial lookup level. For these examples, see Full translation flows for VMSAv8-64 address translation.

## K8.1.1 Examples of performing the initial lookup

The address ranges used for the initial translation table lookup depend on the translation granule, as described in:

- Performing the initial lookup using the 4KB translation granule.
- Performing the initial lookup using the 16KB granule.
- Performing the initial lookup using the 64KB translation granule.

## K8.1.1.1 Performing the initial lookup using the 4KB translation granule

This subsection describes examples of the initial lookup when using the 4KB translation granule that VMSAv8-64 Stage 2 address translation using the 4KB translation granule describes as starting at level 0 or at level 1. It includes those stage 2 translations where concatenation of translation tables is required for the lookup to start at level 1. This means that it gives specific examples of the mechanisms described in Translation process.

Note

For stage 2 translations, the same principles apply to an initial lookup that VMSAv8-64 Stage 2 address translation using the 4KB translation granule describes as starting at level 1. In this case, for some IA sizes concatenation of translation tables means the lookup can, instead, start at level 2.

The following subsections describe these examples of the initial lookup:

- Initial lookup at level 0, 4KB translation granule.
- Initial lookup at level 1, 4KB translation granule.

In all cases, for a stage 2 translation, the VTCR\_EL2.SL0 field must indicate the required initial lookup level, and this level must be consistent with the value of the VTCR\_EL2.T0SZ field, see VMSAv8-64 Stage 2 address translation using the 4KB translation granule.

## K8.1.1.1.1 Initial lookup at level 0, 4KB translation granule

This subsection describes initial lookups with an input address width of ( n +1) bits, meaning the input address is IA[ n :0]. As described in VMSAv8-64 translation using the 4KB granule, a stage 1 or stage 2 initial lookup at level 0 is required when 39 ≤ n ≤ 47. For these lookups:

- TTBR\_ELx[47:( n -35)] specify the translation table base address.
- Bits[ n :39] of the input address are bits[( n -36):3] of the descriptor offset in the translation table.

Note

This means that, when the input address width is less than 48 bits:

- The size of the translation table is reduced.
- More low-order bits of the TTBR\_ELx are required to specify the translation table base address.
- Fewer input address bit are used to specify the descriptor offset in the translation table.

For example, if the input address width is 46 bits:

- The translation table size is 1KB.
- TTBR\_ELx bits[47:10] specify the translation table base address.
- Input address bits[45:39] specify bits[9:3] of the descriptor offset.

Figure K8-1 shows this lookup:

Figure K8-1 Initial lookup for VMSAv8-64 using the 4KB granule, starting at level 0

<!-- image -->

## K8.1.1.1.2 Initial lookup at level 1, 4KB translation granule

This subsection describes initial lookups with an input address width of ( n +1) bits, meaning the input address is IA[ n :0].

## For a stage 1 or stage 2 initial lookup at level 1, without use of concatenated translation tables

As described in VMSAv8-64 translation using the 4KB granule, this applies to IA[ n :0], where 30 ≤ n ≤ 38. For these lookups:

- There is a single translation table at this level.
- TTBR\_ELx[47:( n -26)] specify the translation table base address.
- Bits[ n :30] of the input address are bits[( n -27):3] of the descriptor offset in the translation table.

Figure K8-2 shows this lookup:

Figure K8-2 Initial lookup for VMSAv8-64 using the 4KB granule, starting at level 1, without concatenation

<!-- image -->

## For a stage 2 initial lookup at level 1, with concatenated translation tables

As described in VMSAv8-64 Stage 2 address translation using the 4KB translation granule, this applies to IA[ n :0], where 39 ≤ n ≤ 42. For these lookups:

- There are 2 ( n -38) concatenated translation tables at this level.
- These concatenated translation tables must be aligned to 2 ( n -38) × 4KB. This means TTBR\_ELx[( n -27):12] must be zero.
- TTBR\_ELx[47:( n -26)] specify the base address of the block of concatenated translation tables.
- Bits[ n :30] of the input address are bits[( n -27):3] of the descriptor offset from the base address of the block of concatenated translation tables.

Figure K8-3 shows this lookup:

Figure K8-3 Initial lookup for VMSAv8-64 using the 4KB granule, starting at level 1, with concatenation

<!-- image -->

## K8.1.1.2 Performing the initial lookup using the 16KB granule

This subsection describes examples of the initial lookup when using the 16KB translation granule that VMSAv8-64 Stage 2 address translation using the 16KB translation granule describes as starting at level 0 or at level 1. It includes

those stage 2 translations where concatenation of translation tables is required for the lookup to start at level 1. This means that it gives specific examples of the mechanisms described in Translation process.

Note

For stage 2 translations, the same principles apply to an initial lookup that VMSAv8-64 Stage 2 address translation using the 16KB translation granule describes as starting at level 1. In this case, for some IA sizes concatenation of translation tables means the lookup can, instead, start at level 2.

The following subsections describe these examples of the initial lookup:

- Initial lookup at level 0, 16KB translation granule.
- Initial lookup at level 1, 16KB translation granule.

In all cases, for a stage 2 translation, the VTCR\_EL2.SL0 field must indicate the required initial lookup level, and this level must be consistent with the value of the VTCR\_EL2.T0SZ field, see VMSAv8-64 Stage 2 address translation using the 16KB translation granule.

## K8.1.1.2.1 Initial lookup at level 0, 16KB translation granule

This subsection describes initial lookups with an input address width of ( n +1) bits, meaning the input address is IA[ n :0]. As described in VMSAv8-64 translation using the 16KB granule, the only case where an address translation using the 16KB granule starts at level 0 is a stage 1 translation of a 48-bit input address, IA[47:0]. For this lookup:

- The required translation table has only two entries, meaning its size is 16 bytes, and it must be aligned to 16 bytes.
- TTBR\_ELx[47:4] specify the translation table base address.
- Bit[47] of the input address is bit[3] of the descriptor offset in the translation table.

Figure K8-4 shows this lookup:

<!-- image -->

## Figure K8-4 Initial lookup for VMSAv8-64 using the 16KB granule, starting at level 0

## K8.1.1.2.2 Initial lookup at level 1, 16KB translation granule

This subsection describes initial lookups with an input address width of ( n +1) bits, meaning the input address is IA[ n :0].

## For a stage 1 or stage 2 initial lookup at level 1, without use of concatenated translation tables

As described in VMSAv8-64 translation using the 16KB granule, this applies to IA[ n :0], where 36 ≤ n ≤ 46. For these lookups:

- There is a single translation table at this level.
- TTBR\_ELx[47:( n -32)] specify the translation table base address.

- Bits[ n :36] of the input address are bits[( n -33):3] of the descriptor offset in the translation table.

Figure K8-5 shows this lookup:

Figure K8-5 Initial lookup for VMSAv8-64 using the 16KB granule, starting at level 1, without concatenation

<!-- image -->

## For a stage 2 initial lookup at level 1, with concatenated translation tables

As described in VMSAv8-64 Stage 2 address translation using the 16KB translation granule, the only case where an address translation using the 16KB granule starts at level 1 because of concatenation of translation tables is a stage 2 translation of a 48-bit input address, IA[47:0]. For this lookup:

- There are two concatenated translation tables at this level.
- These concatenated translation tables must be aligned to 2 × 16KB. This means TTBR\_ELx[14] must be zero.
- TTBR\_ELx[47:15] specify the base address of the block of two concatenated translation tables.
- Bits[47:36] of the input address are bits[14:3] of the descriptor offset from the base address of the block of concatenated translation tables.

Figure K8-6 shows this lookup:

<!-- image -->

Figure K8-6 Initial lookup for VMSAv8-64 using the 16KB granule, starting at level 1, with concatenation

## K8.1.1.3 Performing the initial lookup using the 64KB translation granule

This subsection describes examples of the initial lookup when using the 64KB translation granule that VMSAv8-64 Stage 2 address translation using the 64KB translation granule describes as starting at level 1 or at level 2. It includes

those stage 2 translations where concatenation of translation tables is required for the lookup to start at level 2. This means that it gives specific examples of the mechanisms described in Translation process.

Note

For stage 2 translations, the same principles apply to an initial lookup that VMSAv8-64 Stage 2 address translation using the 64KB translation granule describes as starting at level 2. In this case, for some IA sizes concatenation of translation tables means the lookup can, instead, start at level 3.

The following subsections describe these examples of the initial lookup:

- Initial lookup at level 1, 64KB translation granule.
- Initial lookup at level 2, 64KB translation granule.

In all cases, for a stage 2 translation, the VTCR\_EL2.SL0 field must indicate the required initial lookup level, and this level must be consistent with the value of the VTCR\_EL2.T0SZ field, see VMSAv8-64 Stage 2 address translation using the 64KB translation granule.

## K8.1.1.3.1 Initial lookup at level 1, 64KB translation granule

This subsection describes initial lookups with an input address width of ( n +1) bits, meaning the input address is IA[ n :0]. As described in VMSAv8-64 translation using the 64KB granule, a stage 1 or stage 2 initial lookup at level 1 is required when 42 ≤ n ≤ 47. For these lookups:

- The size of the translation table is 2 ( n -39) bytes. This means the size of the translation table, at this level, is always less than the granule size. The address of this translation table must align to the size of the table.
- Bits[ n :42] of the input address are bits[( n - 39):3] of the descriptor offset in the translation table.
- Bits[47:( n -38)] of the TTBR\_ELx specify the translation table base address.

Figure K8-7 shows this lookup:

<!-- image -->

## Figure K8-7 Initial lookup for VMSAv8-64 using the 64KB granule, starting at level 1

## K8.1.1.3.2 Initial lookup at level 2, 64KB translation granule

This subsection describes initial lookups with an input address width of ( n +1) bits, meaning the input address is IA[ n :0].

For a stage 1 or stage 2 initial lookup at level 2, without the use of concatenated translation tables

As described in VMSAv8-64 translation using the 64KB granule, this applies to IA[ n :0], where 29 ≤ n ≤ 41. For these lookups:

- There is a single translation table at this level.

- TTBR\_ELx[47:( n -25)] of the specify the translation table base address.
- Bits[ n :29] of the input address are bits[( n -26):3] of the descriptor offset in the translation table.

Figure K8-8 shows this lookup:

Figure K8-8 Initial lookup for VMSAv8-64 using the 64KB granule, starting at level 2, without concatenation

<!-- image -->

## For a stage 2 initial lookup at level 2, with concatenated translation tables

As described in VMSAv8-64 Stage 2 address translation using the 64KB translation granule, this applies to IA[ n :0], where 42 ≤ n ≤ 45. For these lookups:

- There are 2 ( m -41) concatenated translation tables at this level.
- These concatenated translation tables must be aligned to 2 ( m -41) × 64KB. This means TTBR\_ELx[( n -26):16] must be zero.
- TTBR\_ELx[47:( n -25)] specify the base address of the block of translation tables.
- Bits[ n :42] of the input address are bits[( n -26):16] of the descriptor offset from the base address of the block of translation tables.

Figure K8-9 shows this lookup:

Figure K8-9 Initial lookup for VMSAv8-64 using the 64KB granule, starting at level 2, with concatenation

<!-- image -->

## K8.1.2 Full translation flows for VMSAv8-64 address translation

In a translation table walk, only the first lookup uses the translation table base address from the appropriate TTBR\_ELx. Subsequent lookups use a combination of address information from:

- The table descriptor read in the previous lookup.
- The input address.

This section describes example full translation flows, from the initial lookup to the address of a memory page. The example flows:

- Resolve the maximum-sized IA range supported by the initial lookup level.
- Do not have any concatenation of translation tables.
- Cover only the 4KB and the 64KB translation granules.

Examples of performing the initial lookup described how either reducing the IA range or concatenating translation tables affects the initial lookup.

Note

Reducing the IA range or concatenating translation tables affects only the initial lookup.

The following sections describe full VMSAv8-64 translation flows, down to an entry for a memory page:

- The address and properties fields shown in the translation flows.
- Full translation flow using the 4KB granule and starting at level 0.
- Full translation flow using the 4KB granule and starting at level 1.
- Full translation flow using the 64KB granule and starting at level 1.
- Full translation flow using the 64KB granule and starting at level 2.

## K8.1.2.1 The address and properties fields shown in the translation flows

For an EL1&amp;0 stage 1 translation, when EL2 is implemented and enabled in the current Security state:

- Any descriptor address is the IPA of the required descriptor.
- The final output address is the IPA of the block or page.

In these cases, an EL1&amp;0 stage 2 translation is performed to translate the IPA to the required PA.

For all other translations, the final output address is the PA of the block or page, and any descriptor address is the PA of the descriptor.

Properties indicates register or translation table fields that return information, other than address information, about the translation or the targeted memory region. For more information, see Translation table descriptor formats.

## K8.1.2.2 Full translation flow using the 4KB granule and starting at level 0

Figure K8-10 shows the complete translation flow for a stage 1 translation table walk for a 48-bit input address. This lookup must start with a level 0 lookup. For more information about the fields shown in the figure, see The address and properties fields shown in the translation flows.

Figure K8-10 Complete stage 1 translation of a 48-bit address using the 4KB translation granule

<!-- image -->

If the level 1 lookup or level 2 lookup returns a block descriptor then the translation table walk completes at that level.

Figure K8-10 shows a stage 1 translation. The only difference for a stage 2 translation is that bits[63:58] of the Table

descriptors are SBZ.

## K8.1.2.3 Full translation flow using the 4KB granule and starting at level 1

Figure K8-11 shows the complete translation flow for a stage 1 translation table walk for a 39-bit input address. This lookup must start with a level 1 lookup. For more information about the fields shown in the figure, see The address and properties fields shown in the translation flows.

Figure K8-11 Complete stage 1 translation of a 39-bit address using the 4KB translation granule

<!-- image -->

If the level 1 lookup or the level 2 lookup returns a block descriptor then the translation table walk completes at that level.

Figure K8-11 shows a stage 1 translation. The only difference for a stage 2 translation is that bits[63:58] of the Table descriptors are SBZ.

Comparing this translation with the translation for a 48-bit address, shown in Figure K8-10, shows how the translation for the 42-bit address start the same lookup process one stage later.

## K8.1.2.4 Full translation flow using the 64KB granule and starting at level 1

Figure K8-12 shows the complete translation flow for a stage 1 translation table walk for a 48-bit input address. This lookup must start with a level 1 lookup. For more information about the fields shown in the figure, see The address and properties fields shown in the translation flows.

Figure K8-12 Complete stage 1 translation of a 48-bit address using the 64KB translation granule

<!-- image -->

If the level 2 lookup returns a block descriptor then the translation table walk completes at that level.

Figure K8-12 shows a stage 1 translation. The only difference for a stage 2 translation is that bits[63:58] of the Table descriptors are SBZ.

The level 1 lookup resolves only 6 bits of the input address. As described in Performing the initial lookup using the 64KB translation granule, this means:

- The translation table size for this level is only 512 bytes.

- The required translation table alignment for this level is 512 bytes.
- The Base address field in the TTBR\_ELx is extended, at the low-order end, to be bits[47:9].

## K8.1.2.5 Full translation flow using the 64KB granule and starting at level 2

Figure K8-13 shows the complete translation flow for a stage 1 translation table walk for a 42-bit input address. This lookup must start with a level 2 lookup. For more information about the fields shown in the figure, see The address and properties fields shown in the translation flows.

<!-- image -->

If the level 2 lookup returns a block descriptor then the translation table walk completes at that level.

Figure K8-13 shows a stage 1 translation. The only difference for a stage 2 translation is that bits[63:58] of the Table descriptors are SBZ.

Comparing this translation with the translation for a 48-bit address, shown in Figure K8-12, shows:

- The translation for the 42-bit address starts the same lookup process one stage later.
- Because the initial lookup resolves 13 bits of address:
- -The translation table size for this level is 64KB.
- -The required translation table alignment for this level is 64KB.
- -The Base address field in the TTBR\_ELx is bits[47:16].