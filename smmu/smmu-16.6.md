## 16.6 IMPLEMENTATION DEFINED features

## 16.6.1 Configuration and translation cache locking

Note: The lockdown of configuration and translation cache entries is not a feature directly described by the SMMU architecture because cache structures might vary between implementation and entry lockdown might expose this layout to software.

An implementation might support cache locking in an IMPLEMENTATION DEFINED manner using registers in the IMPLEMENTATION DEFINED memory map.

Note: These registers might expose cache contents and provide insertion, probe and invalidation operations.

If an implementation supports translation cache locking, TLB invalidation must be consistent with the Armv8-A rules on locked entries:

- A TLB invalidate-all operation does not invalidate locked entries.
- An implementation might choose to implement TLB invalidate-by-VA or invalidate-by-ASID operations so that they do one of the following:
- -Invalidate locked entries that are explicitly matched by the operation.
- -Do not invalidate locked entries.

A locked TLB entry is not affected by over-invalidation side effects of invalidation operations that do not directly match the entry.

The behavior of CMD\_CFGI\_* commands with respect to locked configuration cache entries is IMPLEMENTATION DEFINED.

See SMMU\_S\_INIT.INV\_ALL, this initialization invalidate-all operation invalidates locked entries.