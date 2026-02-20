## K8.2 AArch32 Address translation examples

The following sections give address translation examples for the VMSAv8-32 address translation formats:

- Address translation examples using the VMSAv8-32 Short descriptor translation table format.
- Address translation examples using the VMSAv8-32 Long descriptor translation table format.

## K8.2.1 Address translation examples using the VMSAv8-32 Short descriptor translation table format

VMSAv8-32 Short-descriptor Translation Table format descriptors describes the memory section and page option for a single VMSAv8-32 address translation. The following sections show the full translation flow for each of these options:

- Translation flow for a Supersection.
- Translation flow for a Section.
- Translation flow for a Large page.
- Translation flow for a Small page.

The address and Properties fields shown in the translation flows summarizes the information returned by the lookup.

## K8.2.1.1 Translation flow for a Supersection

Figure K8-14 shows the complete translation flow for a Supersection. For more information about the fields shown in this figure, see The address and Properties fields shown in the translation flows.

Figure K8-14 VMSAv8-32 Short-descriptor Supersection address translation

<!-- image -->

Note

Figure K8-14 shows how, when the input address, the V A, addresses a Supersection, the top four bits of the Supersection index bits of the address overlap the bottom four bits of the Table index bits. For more information, see Additional requirements for Short-descriptor format translation tables.

## K8.2.1.2 Translation flow for a Section

Figure K8-15 shows the complete translation flow for a Section. For more information about the fields shown in this figure, see The address and Properties fields shown in the translation flows.

Figure K8-15 VMSAv8-32 Short-descriptor Section address translation

<!-- image -->

## K8.2.1.3 Translation flow for a Large page

Figure K8-16 shows the complete translation flow for a Large page. For more information about the fields shown in this figure, see The address and Properties fields shown in the translation flows.

<!-- image -->

Note

Figure K8-16 shows how, when the input address, the VA, addresses a Large page, the top four bits of the page index bits of the address overlap the bottom four bits of the level 1 table index bits. For more information, see Additional requirements for Short-descriptor format translation tables.

## K8.2.1.4 Translation flow for a Small page

Figure K8-17 shows the complete translation flow for a Small page. For more information about the fields shown in this figure, see The address and Properties fields shown in the translation flows.

<!-- image -->

Figure K8-17 VMSAv8-32 Short-descriptor Small page address translation

## K8.2.1.5 The address and Properties fields shown in the translation flows

For the Non-secure PL1&amp;0 stage 1 translation tables:

- Any descriptor address is the IPA of the required descriptor.
- The final output address is the IPA of the Section, Supersection, Large page, or Small page.

In these cases, a PL1&amp;0 stage 2 translation is performed to translate the IPA to the required PA.

Otherwise, the address is the PA of the descriptor, Section, Supersection, Large page, or Small page.

Properties indicates register or translation table fields that return information, other than address information, about the translation or the targeted memory region. For more information, see Information returned by a translation table lookup, and the description of the register or translation table descriptor.

For translations using the Short-descriptor translation table format, VMSAv8-32 Short-descriptor Translation Table format descriptors describes the descriptors formats.

## K8.2.2 Address translation examples using the VMSAv8-32 Long descriptor translation table format

As described in Translation table walks, when using the VMSAv8-32 Long-descriptor translation table format, in a translation table walk, only the first lookup uses the translation table base address from the appropriate TTBR. Subsequent lookups use a combination of address information from:

- The table descriptor read in the previous lookup.
- The input address.

The following sections give examples of full VMSAv8-32 Long-descriptor format address translation flows, down to an entry for a 4KB page:

- Full translation flow, starting at level 1 lookup.
- Full translation flow, starting at level 2 lookup.

The address and Properties fields shown in the translation flows summarizes the information returned by the lookup.

## K8.2.2.1 Full translation flow, starting at level 1 lookup

Figure K8-18 shows the complete translation flow for a VMSAv8-32 Long-descriptor stage 1 translation table walk that starts with a level 1 lookup. For more information about the fields shown in the figure, see The address and Properties fields shown in the translation flows.

Figure K8-18 Complete VMSAv8-32 Long-descriptor format stage 1 translation, starting at level 1

<!-- image -->

If the level 1 lookup or the level 2 lookup returns a block descriptor then the translation table walk completes at that level.

If bits[47:40] of the TTBR or the descriptor are not zero then the lookup will generate an Address size fault, see Address size fault.

Astage 2 translation that starts at a level 1 lookup differs from the translation shown in Figure K8-18 only as follows:

- The possible values of n are 4-13, to support an input address of between 31 and 40 bits.
- Adescriptor and output addresses are always PAs.

## K8.2.2.2 Full translation flow, starting at level 2 lookup

Figure K8-19 shows the complete translation flow for a stage 1 VMSAv8-32 Long-descriptor translation table walk that starts at a level 2 lookup. For more information about the fields shown in the figure, see The address and Properties fields shown in the translation flows.

Figure K8-19 Complete VMSAv8-32 Long-descriptor format stage 1 translation, starting at level 2

<!-- image -->

If the level 2 lookup returns a block descriptor then the translation table walk completes at that level.

If bits[47:40] of the TTBR or the descriptor are not zero then the lookup will generate an Address size fault, see Address size fault.

Astage 2 translation that starts at a level 2 lookup differs from the translation shown in Figure K8-19 only as follows:

- The possible values of n are 7-16, to support an input address of up to 34 bits.
- The descriptor and output addresses are always PAs.

## K8.2.2.3 The address and Properties fields shown in the translation flows

For the Non-secure PL1&amp;0 stage 1 translation:

- Any descriptor address is the IPA of the required descriptor.
- The final output address is the IPA of the block or page.

In these cases, a PL1&amp;0 stage 2 translation is performed to translate the IPA to the required PA.

For all other translations, the final output address is the PA of the block or page, and any descriptor address is the PA of the descriptor.

Properties indicates register or translation table fields that return information, other than address information, about the translation or the targeted memory region. For more information, see Information returned by a translation table lookup, and the description of the register or translation table descriptor.

For translations using the Long-descriptor translation table format, VMSAv8-32 Long-descriptor Translation Table format descriptors describes the descriptors formats.

## Appendix K9 Recommended Upload and Download Processes for External Debug

This appendix contains the following section:

- Using Memory access mode in AArch64 state.

Note

This description is not part of the Arm architecture specification. It is supplementary, for the convenience of developers and users who might find this information useful.