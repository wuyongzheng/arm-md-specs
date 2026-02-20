## G5.3 Translation tables

VMSAv8-32 defines two alternative translation table formats:

## Short-descriptor format

It uses 32-bit descriptor entries in the translation tables, and provides:

- Up to two levels of address lookup.
- 32-bit input addresses.
- Output addresses of up to 40 bits.
- Support for PAs of more than 32 bits by use of supersections, with 16MB granularity.
- Support for No access, Client, and Manager domains.

## Long-descriptor format

It uses 64-bit descriptor entries in the translation tables, and provides:

- Up to three levels of address lookup.
- Input addresses of up to 40 bits, when used for stage 2 translations.
- Output addresses of up to 40 bits.
- 4KB assignment granularity across the entire PA range.
- No support for domains, all memory regions are treated as in a Client domain.
- Fixed 4KB table size, unless truncated by the size of the input address space.

Note

- -Translation with a 40-bit input address range requires two concatenated 4KB top-level tables, aligned to 8KB.
- -The VMSAv8-64 Long-descriptor translation table format is generally similar to this format, but supports input and output addresses of up to 48 bits, and has an assignment granularity and table size defined by its translation granule . This can be 4KB, 16KB, or 64KB. See Translation table descriptor formats.

In all implementations, of the possible address translations shown in Figure G5-2, for stages of address translation that are using AArch32:

- In a particular Security state, the translation tables for the PL1&amp;0 stage 1 translations can use either translation table format, and the TTBCR.EAE field indicates the current translation table format.
- The translation tables for the Non-secure EL2 stage 1 translations, and for the Non-secure PL1&amp;0 stage 2 translations, must use the Long-descriptor translation table format.

Many aspects of performing a translation table walk depend on the current translation table format. Therefore, the following sections describe the two formats, including how the MMU performs a translation table walk for each format:

- The VMSAv8-32 Short-descriptor translation table format.
- The VMSAv8-32 Long-descriptor translation table format.

The following subsections describe aspects of the translation tables and translation table walks, for memory accesses from AArch32 state, that are independent of the translation table format:

- Translation table walks for memory accesses using VMSAv8-32 translation regimes.
- Information returned by a translation table lookup.
- Determining the translation table base address in the VMSAv8-32 translation regimes.
- Control of translation table walks on a TLB miss.
- Access to the Secure or Non-secure PA map.

See also TLB maintenance requirements.

## G5.3.1 Translation table walks for memory accesses using VMSAv8-32 translation regimes

Atranslation table walk occurs as the result of a TLB miss, and starts with a read of the appropriate starting-level translation table. The result of that read determines whether additional translation table reads are required, for this stage of translation, as described in either:

- Translation table walks, when using the VMSAv8-32 Short-descriptor translation table format.
- Translation table walks, when using the VMSAv8-32 Long-descriptor translation table format.

Note

When using the Short-descriptor translation table format, the starting level for a translation table walk is always a level 1 lookup. However, with the Long-descriptor translation table format, the starting-level can be either a level 1or a level 2 lookup.

For the PL1&amp;0 stage 1 translations, SCTLR.EE determines the endianness of the translation table lookups. SCTLR is banked, and therefore the endianness is determined independently for each Security state.

HSCTLR.EE defines the endianness for the Non-secure EL2 stage 1 and Non-secure PL1&amp;0 stage 2 translations.

Note

## Dynamically changing translation table endianness

Because any change to SCTLR.EE or HSCTLR.EE requires synchronization before it is visible to subsequent operations, Arm strongly recommends that:

- SCTLR.EE is changed only when either:
- -Executing in a mode that does not use the translation tables affected by SCTLR.EE.
- -Executing with SCTLR.M set to 0.
- HSCTLR.EE is changed only when either:
- -Executing in a mode that does not use the translation tables affected by HSCTLR.EE.
- -Executing with HSCTLR.M set to 0.

The PA of the base of the starting-level translation table is determined from the appropriate TTBR, see Determining the translation table base address in the VMSAv8-32 translation regimes.

For more information, see Ordering and completion of TLB maintenance instructions.

Translation table walks must access data or unified caches, or data and unified caches, of other agents participating in the coherency protocol, according to the Shareability attributes described in the TTBR. These Shareability attributes must be consistent with the Shareability attributes for the translation tables themselves.

## G5.3.2 Information returned by a translation table lookup

When an associated stage of address translation is enabled, a memory access requires one or more translation table lookups. If the required Translation Table descriptor is not held in a TLB, a translation table walk is performed to obtain the descriptor. A lookup, whether from the TLB or as the result of a translation table walk, returns both:

- An output address that corresponds to the input address for the lookup.
- Aset of properties that correspond to that output address.

The returned properties are classified as providing address map control , access controls , or region attributes . This classification determines how the descriptions of the properties are grouped. The classification is based on the following model:

## Address map control

Memory accesses from Secure state can access either the Secure or the Non-secure address map, as summarized in Access to the Secure or Non-secure PA map.

Memory accesses from Non-secure state can only access the Non-secure address map.

## Access controls

Attributes

Determine whether the PE, in its current state, can access the output address that corresponds to the given input address. If not, an MMU fault is generated and there is no memory access.

Memory access control describes the properties in this group.

Are valid only for an output address that the PE, in its current state, can access. The attributes define aspects of the required behavior of accesses to the target memory region.

Memory region attributes describes the properties in this group.

## G5.3.3 Determining the translation table base address in the VMSAv8-32 translation regimes

On a TLB miss, the VMSA must perform a translation table walk, and therefore must find the base address of the translation table to use for its lookup. A TTBR holds this address. As Figure G5-2 shows:

- For a Non-secure EL2 stage 1 translation, the HTTBR holds the required base address. The HTCR is the control register for these translations.
- For a Non-secure PL1&amp;0 stage 2 translation, the VTTBR holds the required base address. The VTCR is the control register for these translations.
- For a PL1&amp;0 stage 1 translation, either TTBR0 or TTBR1 holds the required base address. The TTBCR is the control register for these translations.

The Non-secure copies of TTBR0, TTBR1, and TTBCR, relate to the Non-secure PL1&amp;0 stage 1 translation. The Secure copies of TTBR0, TTBR1, and TTBCR, relate to the Secure PL1&amp;0 stage 1 translation.

## For the PL1&amp;0 translation table walks:

- TTBR0 can be configured to describe the translation of V As in the entire address map, or to describe only the translation of V As in the lower part of the address map.
- If TTBR0 is configured to describe the translation of V As in the lower part of the address map, TTBR1 is configured to describe the translation of V As in the upper part of the address map.

The contents of the appropriate instance of the TTBCR determine whether the address map is separated into two parts, and where the separation occurs. The details of the separation depend on the current translation table format, see:

- Selecting between TTBR0 and TTBR1, VMSAv8-32 Short-descriptor translation table format.
- Selecting between TTBR0 and TTBR1, VMSAv8-32 Long-descriptor translation table format.

Example G5-1 shows a typical use of the two sets of translation tables:

## Example G5-1 Example use of TTBR0 and TTBR1

An example of using the two TTBRs for PL1&amp;0 stage 1 address translations is:

## TTBR0

TTBR1

Used for process-specific addresses.

Each process maintains a separate level 1 translation table. On a context switch:

- TTBR0 is updated to point to the level 1 translation table for the new context.
- TTBCR is updated if this change changes the size of the translation table.
- The CONTEXTIDR is updated.

TTBCR can be programmed so that all translations use TTBR0 in a manner compatible with architecture versions before Armv6.

Used for operating system and I/O addresses, that do not change on a context switch.

## G5.3.4 Control of translation table walks on a TLB miss

Two fields in the TCR for the translation stage required by a memory access control whether a translation table walk is performed on a TLB miss. These two fields are the:

- PD0 and PD1 fields, on a PE using the Short-descriptor translation table format.
- EPD0 and EPD1 fields, on a PE using the Long-descriptor translation table format.

Note

For the VMSAv8-32 translation regimes, the different field names are because the fields are in different positions in TTBCR, depending on the translation table format.

The effect of these fields is:

If a TLB miss occurs based on TTBRx, a translation table walk is performed. The current Security state

- {E}PDx == 0 determines whether the memory access is Secure or Non-secure.
- {E}PDx == 1 If a TLB miss occurs based on TTBRx, a level 1 Translation fault is returned, and no translation table walk is performed.

## G5.3.5 Access to the Secure or Non-secure PA map

As stated in Address spaces in VMSAv8-32, a PE can access independent Secure and Non-secure address maps. When the PL1 Exception level is using AArch32, these are defined by the translation tables identified by the Secure TTBR0 and TTBR1. In both translation table formats in the Secure translation tables, the NS field in a descriptor indicates whether the descriptor refers to the Secure or the Non-secure address map:

- NS == 0

Access the Secure PA space.

- NS == 1

Access the Non-secure PA space.

Note

In the Non-secure translation tables, the corresponding field is SBZ. Non-secure accesses always access the Non-secure PA space, regardless of the value of this field.

The Long-descriptor translation table format extends this control, adding an NSTable field to the Secure translation tables, as described in Hierarchical control of Secure or Non-secure memory accesses, Long-descriptor format. In the Non-secure translation tables, the corresponding field is SBZ, and Non-secure accesses ignore the value of this field.

The following sections describe the address map controls in the two implementations:

- Control of Secure or Non-secure memory access, VMSAv8-32 Short-descriptor format.
- Control of Secure or Non-secure memory access, VMSAv8-32 Long-descriptor format.

The following subsection gives more information.

## G5.3.5.1 Secure and Non-secure address spaces

EL3 provides two PA spaces, a Secure PA space and a Non-secure PA space.

As described in Access to the Secure or Non-secure PA map, for the PL1&amp;0 stage 1 translations when controlled from an Exception level using AArch32, the registers that control the stage of translation, TTBR0, TTBR1, TTBCR, and TTBCR2 are banked to provide independent Secure and Non-secure instances of the registers, and the Security state of the PE when it performs a memory access whether the Secure or Non-secure instances are used. This means that for stage 1 of the PL1&amp;0 translation regime there are independent Secure and Non-secure translation tables, and translation table walks are made to the PA space corresponding to the Security state of the translation tables used.

For a translation table walk caused by a memory access from Non-secure state, all memory accesses are to the Non-secure address space.

For a translation table walk caused by a memory access from Secure state:

- When address translation is using the Long-descriptor translation table format:
- -The initial lookup performed must access the Secure address space.
- -If a Table descriptor read from the Secure address space has the NSTable field set to 0, then the next level of lookup is from the Secure address space.
- -If a Table descriptor read from the Secure address space has the NSTable field set to 1, then the next level of lookup, and any subsequent level of lookup, is from the Non-secure address space.

For more information, see Control of Secure or Non-secure memory access, VMSAv8-32 Long-descriptor format.

- Otherwise, all memory accesses are to the Secure address space.

## Note

- When executing in Non-secure state, additional translations are supported. For memory accesses from AArch32 state, these are:
- -Non-secure EL2 stage 1 translation.
- -Non-secure PL1&amp;0 stage 2 translation.

These translations can access only the Non-secure address space.

- Asystem implementation can alias parts of the Secure PA space to the Non-secure PA space in an IMPLEMENTATION SPECIFIC way. As with any other aliasing of physical memory, the use of aliases in this way can require the use of cache maintenance instructions to ensure that changes to memory made using one alias of the physical memory are visible to accesses to the other alias of the physical memory.