## D10.6 Physical Tag locations

DJTNRZ

All statements in this section require implementation of FEAT\_MTE2.

## D10.6.1 Accessing Tag locations

| R FHWSD   | A Tag location is an Allocation Tag associated with an address in the PA space.                                                                                   |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R FXRDJ   | An Allocation Tag and a byte at the same PA are separate locations.                                                                                               |
| R VPTKC   | An instruction accessing an Allocation Tag explicitly, or implicitly for a Tag Check operation , accesses a Tag location .                                        |
| R XTTLW   | An implicit or explicit access to an Allocation Tag uses the same translation, and has the same translation effects, as an access to the associated Tag Granule . |
| I VYGYV   | There is no mechanism to generate an access to an Allocation Tag at a PA other than the PA of the start of a Tag Granule .                                        |
| R TQGBX   | If FEAT_RME is implemented, an access to a Tag location is subject to a granule protection check.                                                                 |
| R FWSBS   | If FEAT_MEC is implemented, an access to a Tag location uses the same PA space and MECID as an access to the associated Tag Granule .                             |

## D10.6.2 Allocation Tag Storage

| R NGLPV   | Storage is provided for each Allocation Tag associated with a Tag Granule of Conventional memory. This is Allocation Tag storage .                                                                         |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R BCFRK   | The result of an access to an Allocation Tag where Allocation Tag storage is not provided is IMPLEMENTATION DEFINED.                                                                                       |
|           | D10.6.2.1 Access to Allocation Tag storage at data locations                                                                                                                                               |
| D RQMQH   | The rules in this section only apply if Allocation Tag storage can be accessed using a data memory effect at a separate PA.                                                                                |
| R DYBTN   | It is IMPLEMENTATION DEFINED whether Allocation Tag storage can be accessed using a data memory effect at a separate PA.                                                                                   |
| I RNGQD   | It is not architecturally required for an access to Allocation Tag storage at a Tag location to be coherent with an access to the same Allocation Tag storage at a data memory location.                   |
| R JMJVY   | An access to Allocation Tag storage at a Tag location can be made visible to an access to that same Allocation Tag storage at a data location, and vice versa, by the use of cache maintenance operations. |
| R LMRBP   | If FEAT_RME is implemented, Allocation Tag storage that can be accessed at a data memory location is only accessible at a data memory location in the Root PA space.                                       |
| R TJBLR   | If FEAT_MEC is implemented, if Allocation Tag storage is accessible at a data memory location, that data location is only accessible in the Root PA space, using the default MECID of zero.                |
| I VLYLK   | If FEAT_MEC is implemented, encryption of Allocation Tags in main memory is an optional defense in depth capability for mitigating attempts to read or corrupt tags.                                       |

## D10.6.3 Caching of Allocation Tags

| R PMQPF   | When data is evicted from a cache entry at a cache level, the evicted data can overwrite data in memory that has been written by another observer if either, or any of the following are true:                                                                                                                                                                                                                                                                                                |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R XPPBK   | If Allocation Tag storage is accessible at a data memory location, when Allocation Tags are evicted from a cache entry at a cache level, the evicted Allocation Tags can overwrite Allocation Tags in memory that have been written by another observer if the Allocation Tags associated with memory within an address range of the size of the Cache Write-Back Granule, and are aligned to that size, have been written by an observer in the Shareability domain of that memory location. |
| R FYDLC   | If an implementation can overwrite Allocation Tags in memory that have been written by another Observer, where the Allocation Tags have not been written by an Observer in the Shareability domain of that memory location, then a cache maintenance operation which:                                                                                                                                                                                                                         |
| R CKJYV   | If a memory region is Untagged , a data cache invalidation operation that would invalidate Allocation Tags in that memory region cleans and invalidates the Allocation Tags .                                                                                                                                                                                                                                                                                                                 |
| I VNMBR   | For more information, see: • Ordering requirements defined by the formal concurrency model.                                                                                                                                                                                                                                                                                                                                                                                                   |