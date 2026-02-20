## D8.18 Caches

## D8.18.1 Data and unified caches

RJHVQL

RCTGML

RNGPVX

IFHPPX

For data and unified caches, if all data accesses to an address do not use mismatched memory attributes, then the use of address translation is transparent to any data access to the address.

For more information, see Mismatched memory attributes.

For data accesses from the same observer to different V As, if the accesses are translated to the same PA with the same memory attributes, then they are coherent and all of the following behaviors are guaranteed without requiring the use of

barrier or cache maintenance instructions:

- Two writes to the same PA occur in program order.
- Aread of a PA returns the value of the last successful write to that PA.
- Awrite to a PA that occurs, in program order, after a read of that PA, has no effect on the value returned by that read.

When cache maintenance is done to a memory location, the effect of that cache maintenance is visible to all V A or IPA aliases of that physical memory location.

The properties of data and unified caches are consistent with implementing the caches as physically-indexed, physically-tagged caches.

## D8.18.2 Instruction caches

| R GXBMD   | An instruction cache has all of the following properties: • An instruction cache is accessed only as a result of an instruction fetch.                                                                                                                                                                                                                                                                                                |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R XBHSB   | The Arm architecture permits all of the following instruction cache implementations: • Physically-indexed, physically-tagged (PIPT) instruction cache. • Virtually-indexed, physically-tagged (VIPT) instruction cache.                                                                                                                                                                                                               |
| I XSPPH   | The CTR_EL0.L1Ip field identifies the form of the instruction caches.                                                                                                                                                                                                                                                                                                                                                                 |
| R WNDVG   | If CTR_EL0.DIC is 1, instruction cache maintenance is not required after overwriting instructions, including for different VA aliases of the affected Locations, regardless of the value of CTR_EL0.L1Ip.                                                                                                                                                                                                                             |
| R XLZJK   | For all permitted instruction cache implementations, the Arm IVIPT Extension is also implemented, which reduces instruction cache maintenance requirements to requiring maintenance only after writing new data to a PA that holds an instruction.                                                                                                                                                                                    |
| I QNJPN   | Previous versions of the Arm architecture permitted an instruction cache option that does not implement the Arm IVIPT Extension.                                                                                                                                                                                                                                                                                                      |
| I GWSPL   | For software to be portable between implementations that might use any of the permitted instruction cache implementations, that software is required to invalidate the instruction cache whenever any condition occurs that requires instruction cache maintenance on at least one of the instruction cache types.                                                                                                                    |
|           | D8.18.2.1 Physically-indexed, physically-tagged instruction caches                                                                                                                                                                                                                                                                                                                                                                    |
| R YXNGL   | For PIPT instruction caches, all of the following apply: • If all instruction fetches to an address do not use mismatched memory attributes, then the use of address translation is transparent to any instruction fetch to the address. • If instruction cache maintenance is done on a memory location, then the effect of that instruction cache maintenance is visible to all VA or IPA aliases of that physical memory location. |

RLYZYY

## D8.18.2.2 Virtually-indexed, physically-tagged instruction caches

For VIPT instruction caches, all of the following apply:

- If all instruction fetches to an address do not use mismatched memory attributes, then the use of address translation is transparent to any instruction fetch to the address.
- If instruction cache maintenance by address is done on a memory location, then the effect of that instruction cache maintenance is visible only to the V A supplied with the operation, and the effect of the invalidation might not be visible to any other V A or IPA aliases of that physical memory location.
- The only architecturally-guaranteed way to invalidate all V A or IPA aliases of a PA from a VIPT instruction cache is to invalidate the entire instruction cache.

## D8.18.3 Cache maintenance requirements due to changing memory region attributes

- IVPPPM If changes are made to the memory region attributes in translation table entries, TLB maintenance might be required. For more information, see TLB maintenance.

IZDQCY

RZNPYM

The behaviors caused by mismatched memory attributes mean that if any of the following changes are made to the Inner Cacheability or Outer Cacheability attributes in translation table entries, then software is required to ensure that any cached copies of affected locations are removed from the caches, typically by cleaning and invalidating the locations from the cache levels that might hold copies of the locations affected by the attribute change:

- Achange from Write-Back to Write-Through.
- Achange from Write-Back to Non-cacheable.
- Achange from Write-Through to Non-cacheable.
- Achange from Write-Through to Write-Back.

For more information, see Mismatched memory attributes and Using break-before-make when updating translation table entries.

If the Shareability attributes in translation table entries are changed, then software is required to execute the following sequence to prevent possible coherency errors caused by mismatched memory attributes:

1. Make the memory location Non-cacheable, Outer Shareable.
2. Clean and invalidate the memory location from caches in the appropriate Shareability domain.
3. Change the Shareability attributes to the new values.