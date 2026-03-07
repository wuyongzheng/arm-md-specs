## Chapter B3

## Command condition functions

This chapter describes functions which are used in command condition expressions.

See also:

- [B1.4 Command condition expressions](rmm-B1.2.md#b14-command-condition-expressions)


## B3.1 AddrInRange function

Returns TRUE if addr is within [base, base+size] .

```
pure func AddrInRange( addr : Address, base : Address, size : integer) => boolean begin return ((UInt(addr) >= UInt(base)) && (UInt(addr) <= UInt(base) + end;
```

```
size));
```

## B3.2 AddrIsAligned function

Returns TRUE if address addr is aligned to an n byte boundary.

```
pure func AddrIsAligned( addr : Address, n : integer) => boolean begin var x : integer = UInt(addr);
```

Chapter B3. Command condition functions B3.3. AddrIsAuxLive function

```
return Align(x, n) == x; end;
```

## B3.3 AddrIsAuxLive function

Returns TRUE if IPA addr is auxiliary-live , that is live in any auxiliary RTT.

```
readonly func AddrIsAuxLive( addr : Address, realm : RmmRealm) =>
```

## B3.4 AddrIsAuxRef function

Returns TRUE if the primary RTT entry at IPA addr is auxiliary-referenced , that is pointed to by an auxiliary RTT entry.

```
readonly func AddrIsAuxRef( addr : Address, realm : RmmRealm) =>
```

```
boolean
```

## B3.5 AddrIsProtected function

## B3.6 AddrIsRmiGranuleAligned function

Returns TRUE if address addr is a Protected IPA for realm pure func AddrIsProtected( addr : Address, realm : RmmRealm) =&gt; boolean begin return UInt(addr) &lt; 2^(realm.ipa\_width -1); end; Returns TRUE if address addr is aligned to the size of an RMI Granule.

```
readonly func AddrIsRmiGranuleAligned( addr : Address) => boolean begin var rmm : RmmGlobal = Rmm(); return AddrIsAligned(addr, rmm.dynamic.rmi_granule_size); end;
```

See also:

- [A2.3.1 Granule size](rmm-A2.3.md#a231-granule-size)

## B3.7 AddrIsRsiGranuleAligned function

Returns TRUE if address addr is aligned to the size of an RSI Granule.

```
readonly func AddrIsRsiGranuleAligned( addr : Address) => boolean begin return AddrIsAligned(addr, RSI_GRANULE_SIZE); end;
```

See also:

```
boolean
```

.

- A2.3.1 Granule size

## B3.8 AddrIsRttLevelAligned function

Returns TRUE if Address addr is aligned to the size of the address range described by an RTTE in a level level RTT.

Returns FALSE if level is invalid.

```
AddrIsRttLevelAligned(
```

```
readonly func addr : Address, level : integer) => boolean
```

## B3.9 AddrIsTrackingRegionAligned function

Returns TRUE if address addr is aligned to the size of a tracking region.

```
readonly func AddrIsTrackingRegionAligned( addr : Address) => boolean begin var rmm : RmmGlobal = Rmm(); return AddrIsAligned(addr, rmm.dynamic.tracking_region_size); end;
```

## B3.10 AddrIsWithin function

Returns TRUE if address addr is within the outer range [base, top) .

```
pure func AddrIsWithin( addr : Address, base : Address, top : Address) => boolean begin var addr_int : integer = var top_int : integer = UInt(top); var base_int : integer = return ((UInt(addr) >= UInt(base)) && (UInt(addr) < UInt(top))); end;
```

```
UInt(addr); UInt(base);
```

## B3.11 AddrRangeIsAuxLive function

Returns TRUE if any IPA in range [base, top) is auxiliary-live , that is live in any auxiliary RTT.

```
readonly func AddrRangeIsAuxLive( base : Address, top : Address, realm : RmmRealm) => boolean
```

## B3.12 AddrRangeIsProtected function

Returns TRUE if all addresses in range [base, top) are Protected IPAs for realm .

```
readonly func AddrRangeIsProtected( base : Address, top : Address, realm : RmmRealm) => boolean
```

Chapter B3. Command condition functions B3.13. AddrRangeIsWithin function

```
begin var size = UInt(top) -UInt(base); return (AddrIsProtected(base, realm) && size > 0 && size < 2^realm.ipa_width && AddrIsProtected(ToAddress(UInt(top) -1), realm)); end;
```

## B3.13 AddrRangeIsWithin function

Returns TRUE if all addresses in the inner range [inner\_base, inner\_top) are within the outer range [outer\_range, outer\_top) .

```
pure func AddrRangeIsWithin( inner_base : Address, inner_top : Address, outer_base : Address, outer_top : Address) => boolean begin return (AddrIsWithin(inner_base, outer_base, outer_top) && AddrIsWithin(inner_top, outer_base, outer_top)); end;
```

B3.14 AddrSetAllDelegableCohDevMem function Returns TRUE if the first size bytes of the Address Set identified by set\_addr and set\_addr\_type are delegable coherent device memory. readonly func AddrSetAllDelegableCohDevMem( set\_desc : RmiAddrSetDesc, set\_addr\_type : RmiRttAddrType, size : integer) =&gt; boolean begin var rmm : RmmGlobal = Rmm(); var offset : integer = 0; while offset &lt; size do var addr : Address = AddrSetEntry(set\_desc, set\_addr\_type, offset); if !PaIsDelegableCohDevMem(addr) then return FALSE; end; offset = offset + rmm.dynamic.rmi\_granule\_size; end; return TRUE; end;

## B3.15 AddrSetAllDelegableNonCohDevMem function

Returns TRUE if the first size bytes of the Address Set identified by set\_addr and set\_addr\_type are delegable non-coherent device memory.

```
readonly func AddrSetAllDelegableNonCohDevMem( set_desc : RmiAddrSetDesc, set_addr_type : RmiRttAddrType, size : integer) => boolean begin
```

Chapter B3. Command condition functions B3.16. AddrSetEntry function

```
var rmm : RmmGlobal = Rmm(); var offset : integer = 0; while offset < size do var addr : Address = AddrSetEntry(set_desc, set_addr_type, offset); if !PaIsDelegableNonCohDevMem(addr) then return FALSE; end; offset = offset + rmm.dynamic.rmi_granule_size; end; return TRUE; end;
```

## B3.16 AddrSetEntry function

Returns address of the offset byte within the Address Set identified by set\_addr and set\_addr\_type .

```
readonly func AddrSetEntry( set_desc : RmiAddrSetDesc, set_addr_type : RmiRttAddrType, offset : integer) => Address
```

## B3.17 AlignDownToRttLevel function

Round down addr to align to the size of the address range described by an RTTE in a level level RTT.

```
readonly func addr : Address, level : integer) => Address
```

## B3.18 AlignUpToRttLevel function

Round up addr to align to the size of the address range described by an RTTE in a level level RTT.

```
AlignDownToRttLevel(
```

```
readonly func AlignUpToRttLevel( addr : Address, level : integer) => Address
```

## B3.19 AnyRecRunning function

Returns TRUE if the state of any REC owned by realm is REC\_RUNNING.

```
readonly func AnyRecRunning( realm : RmmRealm) =>
```

## See also:

- [A2.4 Realm Execution Context](rmm-A2.4.md)
- [B4.5.48 RMI\_REALM\_TERMINATE command](rmm-B4.5.48.md)
- [D1.2.5 Realm destruction flow](rmm-D1.2.md#d125-realm-destruction-flow)

## B3.20 AttestationTokenMaxSize function

Maximum size of attestation token in bytes.

readonly impdef func AttestationTokenMaxSize(

```
boolean
```

```
realm : RmmRealm) => integer
```

## B3.21 AttestationTokenWrite function

Write fragment of attestation token.

Returns amount of data written in bytes.

```
AttestationTokenWrite(
```

```
readonly func addr : Address, offset : integer, size : integer) => integer
```

## B3.22 CmemAt function

Returns the CMEM object located at physical address addr .

```
readonly func CmemAt(
```

```
addr : Address) => RmmCmem
```

## B3.23 CmemAuxCount function

Returns the number of auxiliary Granules required for a CMEM with the specified flags.

The return value is guaranteed not to be greater than 16.

For a given flags value, this function always returns the same value.

```
readonly impdef func CmemAuxCount( flags : RmiCmemFlags) =>
```

## B3.24 CmemMecUpdateComplete function

Returns TRUE if PDEV MEC refresh has been completed for Realm realm on all PDEVs for which all of the following are true:

- The PDEV is a member of a CMEM Interleave Set.

integer

- Per-Realm encryption is enabled on the CMEM Interleave Set.

```
readonly impdef func CmemMecUpdateComplete( realm : RmmRealm) => boolean
```

See also:

- [A11.1.2 MEC and CMEM devices](rmm-A11.md#a1112-mec-and-cmem-devices)

## B3.25 CmemNumPdevs function

Returns the number of PDEVs bound to a CMEM.

```
pure func CmemNumPdevs( cmem : RmmCmem) => integer begin var result : integer = 0; for i = 0 to 7 do if (cmem.pdev[[i]].valid == RMM_TRUE) then result = result + 1; end; end;
```

Chapter B3. Command condition functions

```
B3.26. CurrentRealm function result;
```

```
return end;
```

## B3.26 CurrentRealm function

Returns the current Realm.

```
readonly func CurrentRealm() => RmmRealm
```

## B3.27 CurrentRec function

```
Returns the current REC.
```

```
readonly func CurrentRec() => RmmRec
```

## B3.28 DeviceCommunicate function

Process device communication data and return the new state of the device transaction.

## B3.29 DptEntryCanDescribe function

Returns TRUE if the L0DPT has been created and the size of the DPT entry for address addr is not larger than

```
readonly func DptEntryCanDescribe( addr : Address, size : integer) => boolean begin var rmm : RmmGlobal = Rmm(); // Check that L0DPT has been created if (DptL0().state != DPT_L0_VALID) then return FALSE; end; var l0_entry : RmmDptL0Entry = DptL0Walk(addr); case l0_entry.state of when DPT_L0_ENTRY_BLOCK => return (rmm.static.l0dptsz > size); when DPT_L0_ENTRY_TABLE => return (rmm.dynamic.rmi_granule_size > size); end; return TRUE; end;
```

```
readonly func DeviceCommunicate( pdev : RmmPdev, data : RmiDevCommData) => RmmDevCommState readonly func DeviceCommunicate( vdev : RmmVdev, data : RmiDevCommData) => RmmDevCommState readonly func DeviceCommunicate( vdev : RmmVdev) => RmmDevCommState size .
```

## B3.30 DptL0 function

Returns the Level 0 DPT.

```
This is a system-wide singleton. readonly func DptL0() => RmmDptL0
```

## B3.31 DptL0Walk function

Returns the Level 1 DPT which describes the physical address region starting from addr .

```
readonly func DptL0Walk( addr : Address) =>
```

```
RmmDptL0Entry
```

## B3.32 Equal function

Check whether concrete and abstract values are equal

```
pure func Equal( abstract : RmmFeature, concrete : RmiFeature) => boolean pure func Equal( concrete : RmiFeature, abstract : RmmFeature) => boolean pure func Equal( abstract : RmmHashAlgorithm, concrete : RmiHashAlgorithm) => boolean pure func Equal( concrete : RmiHashAlgorithm, abstract : RmmHashAlgorithm) => boolean pure func Equal( abstract : RmmLfaPolicy, concrete : RmiLfaPolicy) => boolean pure func Equal( concrete : RmiLfaPolicy, abstract : RmmLfaPolicy) => boolean pure func Equal( abstract : RmmMecPolicy, concrete : RmiMecPolicy) => boolean pure func Equal( concrete : RmiMecPolicy, abstract : RmmMecPolicy) => boolean pure func Equal( abstract : RmmMemCategory, concrete : RmiMemCategory) => boolean pure func Equal( concrete : RmiMemCategory, abstract : RmmMemCategory) => boolean pure func Equal( abstract : RmmOpCanCancel, concrete : RmiOpCanCancel) => boolean pure func Equal( concrete : RmiOpCanCancel,
```

| abstract                               | : RmmOpCanCancel) => boolean                                      |
|----------------------------------------|-------------------------------------------------------------------|
| pure func Equal( abstract concrete     | : RmmPdevCategory, : RmiPdevCategory) => boolean                  |
| pure func Equal( concrete : abstract : | RmiPdevCategory, RmmPdevCategory) => boolean                      |
| pure func abstract concrete            | Equal( : RmmPdevSpdm, : RmiPdevSpdm) => boolean                   |
| pure func Equal( concrete : abstract : | RmiPdevSpdm, RmmPdevSpdm) => boolean                              |
| pure func abstract : concrete :        | Equal( RmmPdevState, RmiPdevState) => boolean                     |
| pure func concrete abstract            | Equal( : RmiPdevState, : RmmPdevState) => boolean                 |
| pure func abstract concrete            | Equal( : RmmPdevStreamType, : RmiPdevStreamType) => boolean       |
| pure func concrete abstract             Equal( : RmiPdevStreamType, : RmmPdevStreamType) => boolean |
| pure func abstract concrete            | Equal( : RmmRecRunnable, : RmiRecRunnable) => boolean             |
| pure func concrete : abstract :        | Equal( RmiRecRunnable, RmmRecRunnable) => boolean                 |
| pure func Equal( abstract : concrete : | RmmRipas, RmiRipas) => boolean                                    |
| pure func concrete abstract            | Equal( : RmiRipas, : RmmRipas) => boolean                         |
| pure func abstract concrete            | Equal( : RmmRttPlaneFeature, : RmiRttPlaneFeature) => boolean     |
| pure func Equal( concrete : abstract : | RmiRttPlaneFeature, RmmRttPlaneFeature) => boolean                |
| pure func abstract concrete            | Equal( : RmmRttS2APBase, : RmiRttS2APBase) => boolean             |

| pure func Equal( concrete : abstract :   | RmiRttS2APBase, RmmRttS2APBase) => boolean                     |
|------------------------------------------|----------------------------------------------------------------|
| pure func Equal( abstract : concrete :   | RmmRttS2APEncoding, RmiRttS2APEncoding) => boolean             |
| pure func Equal( concrete abstract       | : RmiRttS2APEncoding, : RmmRttS2APEncoding) => boolean         |
| pure func Equal( abstract concrete       | : RmmTrackingRegionState, : RmiTrackingRegionState) => boolean |
| pure func Equal( concrete : abstract :   | RmiTrackingRegionState, RmmTrackingRegionState) => boolean     |
| pure func abstract concrete              | Equal( : RmmVdevState, : RmiVdevState) => boolean              |
| pure func Equal( concrete : abstract : :  RmiVdevState, RmmVdevState) => boolean                   |
| pure func Equal( abstract : concrete     | RmmFeature, RsiFeature) => boolean                             |
| pure func Equal( concrete : abstract :   | RsiFeature, RmmFeature) => boolean                             |
| pure func abstract concrete              | Equal( : RmmHashAlgorithm, : RsiHashAlgorithm) => boolean      |
| pure func concrete abstract              | Equal( : RsiHashAlgorithm, : RmmHashAlgorithm) => boolean      |
| pure func Equal( abstract : concrete :   | RmmRipas, RsiRipas) => boolean                                 |
| pure func Equal( concrete : abstract :   | RsiRipas, RmmRipas) => boolean                                 |
| pure func Equal( abstract : concrete :   | RmmRipasChangeDestroyed, RsiRipasChangeDestroyed) => boolean   |
| pure func Equal( concrete : abstract :   | RsiRipasChangeDestroyed, RmmRipasChangeDestroyed) => boolean   |

## B3.33 FeatureToRmi function

Convert feature bit to RMI type.

```
readonly func FeatureToRmi( value : RmmFeature) => RmiFeature begin case value of when FEATURE_FALSE => return RMI_FEATURE_FALSE; when FEATURE_TRUE => return RMI_FEATURE_TRUE; end; end;
```

## B3.34 FeatureToRsi function

Convert feature bit to RSI type.

```
readonly func FeatureToRsi( value : RmmFeature) => RsiFeature begin case value of when FEATURE_FALSE => return when FEATURE_TRUE => return RSI_FEATURE_TRUE; end; end;
```

## B3.35 Gicv3ConfigIsValid function

Returns TRUE if ICH\_LR&lt;n&gt;\_EL2.HW == '0' for all implemented values of n .

```
readonly func Gicv3ConfigIsValid() => boolean
```

See also:

- [A6.1 Realm interrupts](rmm-A6.1.md)
- [B4.6.64 RmiRecEnter type](rmm-B4.6.md#b4664-rmirecenter-type)

```
RSI_FEATURE_FALSE;
```

## B3.36 GptL0Walk function

Returns the Level 1 GPT which describes the physical address region starting from addr .

```
readonly func GptL0Walk( addr : Address) =>
```

```
RmmGptL0Entry
```

## B3.37 GptL1IsHomogeneous function

Returns TRUE if the Level 1 GPT which describes the physical address region starting from addr is homogeneous.

```
readonly func GptL1IsHomogeneous( addr : Address) => boolean
```

## B3.38 GranuleAt function

Returns the Granule located at physical address addr .

```
readonly func GranuleAt( addr : Address) => RmmGranule
```

Chapter B3. Command condition functions B3.39. GranulesAllState function

See also:

- [A2.3 Physical memory](rmm-A2.3.md)

## B3.39 GranulesAllState function

Returns TRUE if the state of all Granules within the range [base, top) or [base, base + size) is equal to state .

```
readonly func GranulesAllState( base : Address, top : Address, state : RmmGranuleState) => boolean readonly func GranulesAllState( base : Address, size : integer, state : RmmGranuleState) => boolean
```

## B3.40 GranulesAllStateList function

Returns TRUE if the state of all Granules within the first size bytes of the address set described by an RMI Address List stored at PA alist is equal to state .

```
readonly func GranulesAllStateList( alist : Address, size : integer, state : RmmGranuleState) =>
```

## B3.41 GranuleSizeFromRmi function

## Decodes a Granule size.

```
readonly func GranuleSizeFromRmi( size : RmiGranuleSize) => integer begin case size of when RMI_GRANULE_SIZE_4KB => return 4 * when RMI_GRANULE_SIZE_16KB => return 16 * when RMI_GRANULE_SIZE_64KB => return 64 * end; end;
```

## B3.42 GranuleSizeToRmi function

Encodes a Granule size.

```
readonly func GranuleSizeToRmi( size : integer) => RmiGranuleSize begin case size of when 4 * KB => return RMI_GRANULE_SIZE_4KB; when 16 * KB => return RMI_GRANULE_SIZE_16KB; when 64 * KB => return RMI_GRANULE_SIZE_64KB; end; end;
```

```
boolean
```

```
KB; KB; KB;
```

## B3.43 HdmAddressRangeIsFree function

Returns TRUE if address range range is free in the HDM decoder associated with cmem .

```
readonly func HdmAddressRangeIsFree( cmem : RmmCmem, range : RmiAddrRange) => boolean readonly func HdmAddressRangeIsFree( cmem : RmmCmem, range : RmmAddrRange) => boolean
```

## B3.44 HdmDecoderIsFree function

Returns TRUE if the specified HDM decoder is free.

```
readonly func HdmDecoderIsFree( cmem : RmmCmem, decoder_id : bits(8)) =>
```

```
readonly func HdmDecoderIsFree( pdev : RmmPdev, decoder_id : bits(8)) =>
```

```
boolean boolean
```

## B3.45 MecidAvailable function

Returns TRUE if a MEC is available which satisfies policy .

```
readonly func MecidAvailable( policy : RmiMecPolicy) =>
```

See also:

- [Chapter A11 Realm memory encryption](rmm-A11.md)

## B3.46 MemCategoryIsCompatible function

boolean

Returns TRUE if the specified memory category is compatible with the system memory layout view for the specified address.

```
readonly impdef func MemCategoryIsCompatible( category : RmiMemCategory, addr : Address) => boolean
```

See also:

- [A2.3.2 Views of physical memory](rmm-A2.3.md#a232-views-of-physical-memory)

## B3.47 MemPermLabelSupported function

Returns TRUE if the specified value is a valid encoding for a memory permission label and the label is supported by the implementation.

```
MemPermLabelSupported(
```

```
readonly impdef func label : bits(64)) => boolean
```

## B3.48 MinAddress function

Returns the smaller of two addresses.

```
readonly func MinAddress( addr1 : Address, addr2 : Address) => Address begin return ToAddress(Min(UInt(addr1), UInt(addr2))); end;
```

## B3.49 MpidrEqual function

Returns TRUE if the specified MPIDR values are logically equivalent.

## B3.50 MpidrIsUsed function

## B3.51 MsiAddrIsValid function

pure func MpidrEqual( rmm\_mpidr : bits(64), rmi\_mpidr : RmiRecMpidr) =&gt; boolean begin return (rmm\_mpidr[ 3: 0] == rmi\_mpidr.aff0 &amp;&amp; rmm\_mpidr[15: 8] == rmi\_mpidr.aff1 &amp;&amp; rmm\_mpidr[23:16] == rmi\_mpidr.aff2 &amp;&amp; rmm\_mpidr[31:24] == rmi\_mpidr.aff3); end; Returns TRUE if the specified MPIDR value identifies a REC in the current Realm. readonly func MpidrIsUsed( mpidr : bits(64)) =&gt; boolean Returns TRUE if addr is a valid MSI address.

```
readonly func MsiAddrIsValid( addr : Address) => boolean
```

## B3.52 NonSecureAccessPermitted function

Returns TRUE if the Granule located at physical address addr is accessible via Non-secure PAS.

```
NonSecureAccessPermitted(
```

```
readonly func addr : Address) => boolean
```

## B3.53 OperationCanCancel function

Returns whether the operation identified by handle can be cancelled.

```
readonly impdef func OperationCanCancel( handle : bits(64)) => RmmOpCanCancel
```

See also:

- [B4.3.2 Stateful RMI operations](rmm-B4.3.md#b432-stateful-rmi-operations)

## B3.54 OperationIncomplete function

Returns TRUE if the operation identified by handle results in an intermediate state.

```
OperationIncomplete(
```

```
readonly impdef func handle : bits(64)) => boolean
```

See also:

- [B4.3.2 Stateful RMI operations](rmm-B4.3.md#b432-stateful-rmi-operations)

## B3.55 PaAllDelegableConventional16 function

Returns TRUE if the first count entries in a list addresses are delegable conventional memory.

```
readonly func PaAllDelegableConventional16( addr : array [[16]] of Address, count : integer) => boolean begin assert 0 <= count && count <= 16; for i = 0 to count -1 do if !PaIsDelegableConventionalFine(addr[[i]]) return FALSE; end; end; return TRUE; end;
```

## B3.56 PaAllDelegableConventional32 function

Returns TRUE if the first count entries in a list addresses are delegable conventional memory.

```
readonly func PaAllDelegableConventional32( addr : array [[32]] of Address, count : integer) => boolean begin assert 0 <= count && count <= 32; for i = 0 to count -1 do if !PaIsDelegableConventionalFine(addr[[i]]) then return FALSE; end; end; return TRUE; end;
```

```
then
```

## B3.57 PaIsCohDevMem function

Returns TRUE if the Granule located at physical address addr is within a region of the system memory map which is reserved for coherent device memory.

Note that a TRUE return value does not indicate whether the RMM has verified a device which is mapped at this address.

```
PaIsCohDevMem(
```

```
readonly impdef func addr : Address) => boolean
```

## See also:

- [A2.3.2 Views of physical memory](rmm-A2.3.md#a232-views-of-physical-memory)

Chapter B3. Command condition functions B3.58. PaIsDelegable function

## B3.58 PaIsDelegable function

Returns TRUE if the Granule located at physical address addr is delegable memory.

```
readonly func PaIsDelegable( addr : Address) => boolean begin return (PaIsDelegableDevMem(addr) || PaIsDelegableConventionalFine(addr)); end;
```

## See also:

- [A2.3.5 Delegable physical memory](rmm-A2.3.md#a235-delegable-physical-memory)

## B3.59 PaIsDelegableCohDevMem function

Returns TRUE if the Granule located at physical address addr is delegable coherent device memory.

## B3.60 PaIsDelegableConventional function

Returns TRUE if the Granule located at physical address addr is delegable conventional memory.

```
readonly func PaIsDelegableConventional( addr : Address) => boolean begin var region : RmmTrackingRegion = TrackingRegionAt(addr); return (PaIsDram(addr) && PaIsTracked(addr)) || (PaIsDelegableCohDevMem(addr) && region.category == MEM_CATEGORY_CONVENTIONAL); end;
```

- readonly func PaIsDelegableCohDevMem( addr : Address) =&gt; boolean begin return (PaIsCohDevMem(addr) &amp;&amp; PaIsPopulated(addr) &amp;&amp; PaIsTracked(addr)); end; See also: · A2.3.5 Delegable physical memory

## See also:

- [A2.3.5 Delegable physical memory](rmm-A2.3.md#a235-delegable-physical-memory)

## B3.61 PaIsDelegableConventionalFine function

Returns TRUE if the Granule located at physical address addr is delegable conventional memory and is fine-grained tracked.

```
readonly func PaIsDelegableConventionalFine( addr : Address) => boolean begin var region : RmmTrackingRegion = TrackingRegionAt(addr);
```

Chapter B3. Command condition functions B3.62. PaIsDelegableDevMem function

```
return (PaIsDelegableConventional(addr) && (region.state == TRACKING_FINE)); end;
```

## B3.62 PaIsDelegableDevMem function

Returns TRUE if the Granule located at physical address addr is delegable device memory.

```
readonly func PaIsDelegableDevMem( addr : Address) => boolean begin return (PaIsDelegableCohDevMem(addr) || PaIsDelegableNonCohDevMem(addr)); end;
```

## See also:

- [A2.3.5 Delegable physical memory](rmm-A2.3.md#a235-delegable-physical-memory)

## B3.63 PaIsDelegableNonCohDevMem function

Returns TRUE if the Granule located at physical address addr is delegable non-coherent device memory.

```
readonly func addr : Address) => boolean begin return (PaIsNonCohDevMem(addr) && PaIsPopulated(addr) && PaIsTracked(addr)); end;
```

## See also:

- [A2.3.5 Delegable physical memory](rmm-A2.3.md#a235-delegable-physical-memory)

## B3.64 PaIsDram function

```
PaIsDelegableNonCohDevMem(
```

Returns TRUE if the Granule located at physical address addr is within a region of the system memory map which is backed by DRAM.

```
readonly impdef func PaIsDram( addr : Address) => boolean
```

## See also:

- [A2.3.2 Views of physical memory](rmm-A2.3.md#a232-views-of-physical-memory)

## B3.65 PaIsNonCohDevMem function

Returns TRUE if the Granule located at physical address addr is within a region of the system memory map which is reserved for non-coherent device memory.

Note that a TRUE return value does not indicate whether the RMM has verified a device which is mapped at this address.

```
PaIsNonCohDevMem(
```

```
readonly impdef func addr : Address) => boolean
```

## See also:

- [A2.3.2 Views of physical memory](rmm-A2.3.md#a232-views-of-physical-memory)

## B3.66 PaIsPopulated function

Returns TRUE if physical address addr is backed by a resource which has been verified by the RMM.

```
readonly func PaIsPopulated( addr : Address) =>
```

## See also:

- [A2.3.3 Populated physical memory](rmm-A2.3.md#a233-populated-physical-memory)
- [B3.67 PaIsTracked function](rmm-B3.md#b367-paistracked-function)

## B3.67 PaIsTracked function

Returns TRUE if the tracking region which includes address addr is tracked.

Note that a TRUE return value does not indicate whether the address is backed by a resource which has been verified by the RMM.

- readonly func PaIsTracked( addr : Address) =&gt; boolean begin var region : RmmTrackingRegion = TrackingRegionAt(addr); return (region.state == TRACKING\_COARSE || region.state == TRACKING\_FINE); end; See also: · A2.3.4 Granule tracking region · B3.66 PaIsPopulated function

## B3.68 PaIsTrackedFine function

Returns TRUE if the tracking region which includes address addr is tracked at fine granularity.

Note that a TRUE return value does not indicate whether the address is backed by a resource which has been verified by the RMM.

```
readonly func PaIsTrackedFine( addr : Address) => boolean begin var region : RmmTrackingRegion = TrackingRegionAt(addr); return region.state == TRACKING_FINE; end;
```

## B3.69 PaRangeIsPopulated function

Returns TRUE if all physical addresses within the range [base, top) are backed by resources which have been verified by the RMM.

```
readonly func PaRangeIsPopulated( base : Address,
```

```
boolean
```

```
top : Address) => boolean
```

See also:

- [A2.3.3 Populated physical memory](rmm-A2.3.md#a233-populated-physical-memory)

## B3.70 PaRangeIsUnpopulated function

Returns TRUE if no physical addresses within the range [base, top) are backed by resources which have been verified by the RMM.

```
PaRangeIsUnpopulated(
```

```
readonly func base : Address, top : Address) => boolean
```

See also:

- [A2.3.3 Populated physical memory](rmm-A2.3.md#a233-populated-physical-memory)

## B3.71 PdevAt function

Returns the PDEV object located at physical address addr .

```
readonly func PdevAt( addr : Address) =>
```

## B3.72 PdevFlags function

Get RmiPdevFlags value.

```
readonly func PdevFlags( pdev : RmmPdev) => RmiPdevFlags begin var flags : RmiPdevFlags; case pdev.spdm of when SPDM_FALSE => flags.spdm = when SPDM_TRUE => flags.spdm = RMI_SPDM_TRUE; end; return flags; end;
```

```
RmmPdev RMI_SPDM_FALSE;
```

## B3.73 PdevIsBusy function

Returns TRUE if the PDEV object is currently unable to service a request for an IMPLEMENTATION DEFINED reason.

```
readonly impdef func PdevIsBusy( pdev : RmmPdev) => boolean
```

## B3.74 PdevRidRangeOverlap function

Returns TRUE if the RID range of pdev overlaps the RID range of any other protected PDEV within the same PCIe segment.

```
PdevRidRangeOverlap(
```

```
readonly impdef func pdev : RmmPdev) => boolean
```

## B3.75 PdevStreamAlloc function

Allocate a PDEV stream handle for the specified pair of PDEVs.

If a free handle is available, result.valid is TRUE and result.stream.state is PDEV\_STREAM\_DISCONNECTED.

```
readonly func PdevStreamAlloc( pdev_1 : RmmPdev, pdev_2 : RmmPdev) =>
```

```
RmmPdevStreamResult
```

## B3.76 PdevStreamFromHandle function

Returns PDEV stream.

```
readonly func PdevStreamFromHandle( pdev : RmmPdev, stream_hnd : bits(64)) =>
```

```
readonly func PdevStreamFromHandle( pdev_1 : RmmPdev, pdev_2 : RmmPdev, stream_hnd : bits(64)) =>
```

```
RmmPdevStreamResult RmmPdevStreamResult
```

## B3.77 PdevStreamFromType function

## B3.78 PdevStreamLive function

Query whether the specified PDEV(s) have a stream of type stream\_type . readonly func PdevStreamFromType( pdev : RmmPdev, stream\_type : RmmPdevStreamType) =&gt; RmmPdevStreamResult readonly func PdevStreamFromType( pdev\_1 : RmmPdev, pdev\_2 : RmmPdev, stream\_type : RmmPdevStreamType) =&gt; RmmPdevStreamResult

Returns TRUE if pdev has any connected PDEV streams.

```
readonly func PdevStreamLive( pdev : RmmPdev) => boolean
```

## B3.79 PdevStreamPdev2Category function

Returns category of pdev\_2 for the specified PDEV stream type.

```
readonly func PdevStreamPdev2Category( stream_type : RmiPdevStreamType) => RmmPdevCategory begin case stream_type of when RMI_PDEV_STREAM_NON_TEE => return PDEV_ROOT_PORT; when RMI_PDEV_STREAM_NCOH => return PDEV_ROOT_PORT; when RMI_PDEV_STREAM_COH => return PDEV_ROOT_PORT; when RMI_PDEV_STREAM_COH_CMEM => return PDEV_ROOT_PORT; when RMI_PDEV_STREAM_NCOH_P2P => return PDEV_ENDPOINT_ACCEL_OFF_CHIP; otherwise => unreachable; end; end;
```

## B3.80 PdevStreamPdev2Required function

Returns TRUE if pdev\_2 is required for the specified PDEV stream type.

```
readonly func PdevStreamPdev2Required( stream_type : RmmPdevStreamType) => boolean begin case stream_type of when PDEV_STREAM_NCOH_SYS => return FALSE; when PDEV_STREAM_COH_SYS => return FALSE; otherwise => return TRUE; end; end; readonly func PdevStreamPdev2Required( stream_type : RmiPdevStreamType) => boolean begin return PdevStreamPdev2Required( PdevStreamTypeFromRmi(stream_type)); end;
```

## B3.81 PdevStreamsForVdev function

Returns TRUE if pdev has the required set of streams for VDEV creation.

```
readonly func PdevStreamsForVdev( pdev : RmmPdev) => boolean
```

See also:

- [A9.3 Physical device stream object](rmm-A9.3.md)

## B3.82 PdevStreamTypeFromRmi function

Convert stream type enumeration.


```
readonly func PdevStreamTypeFromRmi( stream_type : RmiPdevStreamType) => RmmPdevStreamType begin case stream_type of when RMI_PDEV_STREAM_NON_TEE => return PDEV_STREAM_NON_TEE; when RMI_PDEV_STREAM_NCOH => return PDEV_STREAM_NCOH; when RMI_PDEV_STREAM_COH => return PDEV_STREAM_COH; when RMI_PDEV_STREAM_COH_CMEM => return PDEV_STREAM_COH_CMEM; when RMI_PDEV_STREAM_NCOH_P2P => return PDEV_STREAM_NCOH_P2P; when RMI_PDEV_STREAM_NCOH_SYS => return PDEV_STREAM_NCOH_SYS; when RMI_PDEV_STREAM_COH_SYS => return PDEV_STREAM_COH_SYS; end; end;
```

## B3.83 PdevVsmmuIsCompatible function

Returns TRUE if the attributes of vsmmu are compatible with pdev .

If the PSMMU associated with the PDEV does not support two stages of translation, this function returns FALSE .

```
readonly func PdevVsmmuIsCompatible( pdev : RmmPdev, vsmmu : RmmVsmmu) => boolean
```

## B3.84 PlaneSysregValid function

Whether addr identifies an accessible Plane system register.

If addr.d128 is TRUE and either of the following is false then the function returns FALSE.

- FEAT\_SYSREG128 is implemented
- addr identifies a 128-bit system register

```
readonly func PlaneSysregValid( rec : RmmRec, addr : RsiSysregAddress, op : RmmReadWriteOp) => boolean
```

## B3.85 PlaneSysregValue function

Value of a Plane system register.

```
readonly func PlaneSysregValue( rec : RmmRec, plane_idx : integer, addr : RsiSysregAddress) =>
```

```
bits(128)
```

## B3.86 PsciReturnCodeEncode function

```
Return encoding for a PsciReturnCode value.
```

```
pure func PsciReturnCodeEncode( value : PsciReturnCode) =>
```

## B3.87 PsciReturnCodePermitted function

Whether a PSCI return code is permitted.

```
readonly func PsciReturnCodePermitted( calling_rec : RmmRec, target_rec : RmmRec, value : PsciReturnCode) => boolean begin if value == PSCI_SUCCESS then return TRUE; end; var fid : bits(64) = calling_rec.gprs[[0]]; // Host is permitted to deny a PSCI_CPU_ON request, if the target // CPU is not already on. if (fid == FID_PSCI_CPU_ON && target_rec.flags.runnable != RUNNABLE && value == PSCI_DENIED) then return TRUE; end; return FALSE; end;
```

## See also:

- [A4.3.7 REC exit due to PSCI](rmm-A4.3.md#a437-rec-exit-due-to-psci)

bits(64)

- B4.5.38 RMI\_PSCI\_COMPLETE command

## B3.88 PsciVersion function

```
PSCI version.
```

```
readonly func PsciVersion() => PsciInterfaceVersion
```

## B3.89 PsmmuAddrIsValid function

Returns TRUE if addr is the base address of a PSMMU.

```
readonly func PsmmuAddrIsValid( addr : Address) => boolean
```

## B3.90 PsmmuAt function

Returns the PSMMU object located at physical address addr

```
readonly func PsmmuAt( addr : Address) =>
```

```
. RmmPsmmu
```

## B3.91 PsmmuCmdQueueFull function

Returns TRUE if the command queue of psmmu

```
readonly func psmmu : RmmPsmmu) =>
```

```
is full. PsmmuCmdQueueFull( boolean
```

## B3.92 PsmmuFromPdev function

Returns the PSMMU which handles transactions from pdev .

```
readonly func PsmmuFromPdev( pdev : RmmPdev) => RmmPsmmu
```


## B3.93 PsmmuL1StIsLive function

Returns TRUE if the PSMMU Level 1 Stream Table is live.

```
readonly func PsmmuL1StIsLive( psmmu : RmmPsmmu) => boolean
```

## See also:

- [A9.7.4 PSMMU Stream Tables](rmm-A9.7.md#a974-psmmu-stream-tables)

## B3.94 PsmmuL2StIsLive function

Returns TRUE if the PSMMU Level 2 Stream Table which describes StreamID range starting at sid is live.

```
readonly func PsmmuL2StIsLive( psmmu : RmmPsmmu, sid : bits(64)) => boolean
```

## See also:

- [A9.7.4 PSMMU Stream Tables](rmm-A9.7.md#a974-psmmu-stream-tables)

## B3.95 PsmmuStWalk function

Returns PSMMU Stream Table walk result for StreamID sid .

```
readonly func PsmmuStWalk( psmmu : RmmPsmmu, sid : bits(64)) =>
```

```
RmmPsmmuStWalkResult
```

## B3.96 PsmmuSupportsMsi function

Returns TRUE if the PSMMU located at addr supports MSI.

```
readonly func PsmmuSupportsMsi( addr : Address) => boolean
```

## B3.97 RealmAt function

Returns the Realm whose RD is located at physical address addr .

```
readonly func RealmAt( addr : Address) =>
```

See also:

- [A2.2 Realm](rmm-A2.2.md)

## B3.98 RealmIpaRangeAllRipasIf function

Returns TRUE if all addresses within IPA range [base, top) for which RIPAS was equal to ripas\_pre in realm\_pre have RIPAS equal to ripas in realm .

```
readonly func realm_pre : RmmRealm, realm : RmmRealm, base : Address, top : Address, ripas_pre : RmmRipas, ripas : RmmRipas) => boolean
```

```
RmmRealm
```

```
RealmIpaRangeAllRipasIf(
```

## B3.99 RealmIsLive function

Returns TRUE if the Realm whose RD is located at physical address addr is live.

```
readonly func RealmIsLive( addr : Address) =>
```

## See also:

- [A2.2.4 Realm liveness](rmm-A2.2.md#a224-realm-liveness)

## B3.100 RealmMeasurementEncode function

Return encoding for an RmmRealmMeasurement value.

```
pure func RealmMeasurementEncode( value : RmmRealmMeasurement) => array [[8]] of
```

```
boolean
```

```
bits(64)
```

## B3.101 RealmParamsSupported function

Returns TRUE if the Realm parameters are supported by the implementation.

```
readonly func RealmParamsSupported( params : RmiRealmParams) => boolean begin var rmm : RmmGlobal = Rmm(); if (params.flags0.lpa2 == RMI_FEATURE_TRUE && rmm.static.feat_lpa2 != FEATURE_TRUE) then return FALSE; end; if (params.flags0.sve == RMI_FEATURE_TRUE && rmm.static.feat_sve != FEATURE_TRUE) then return FALSE; end; if (params.flags0.pmu == RMI_FEATURE_TRUE && rmm.static.feat_pmu != FEATURE_TRUE) then return FALSE; end; if (params.flags0.da == RMI_FEATURE_TRUE && rmm.static.feat_da != FEATURE_TRUE) then return FALSE; end; if (params.flags1.ats == RMI_FEATURE_TRUE && rmm.static.feat_ats != FEATURE_TRUE) then return FALSE; end; if (params.s2sz > rmm.static.max_ipa_width) then return FALSE; end; if (params.sve_vl > rmm.static.max_sve_vl) then return FALSE; end; if (params.num_bps == 0 || params.num_bps + 1 > rmm.static.num_bps) then return FALSE; end; if (params.num_wps == 0 || params.num_wps + 1 > rmm.static.num_wps) then return FALSE; end; if (params.pmu_num_ctrs > rmm.static.pmu_num_ctrs) then return FALSE; end; if (params.hash_algo == RMI_HASH_SHA_256 && rmm.static.feat_sha_256 != FEATURE_TRUE) then return FALSE; end;
```

```
if (params.hash_algo == RMI_HASH_SHA_384 && rmm.static.feat_sha_384 != FEATURE_TRUE) then return FALSE; end; if (params.hash_algo == RMI_HASH_SHA_512 && rmm.static.feat_sha_512 != FEATURE_TRUE) then return FALSE; end; if (params.num_aux_planes > rmm.static.max_num_aux_planes) then return FALSE; end; if (params.flags1.rtt_s2ap_encoding == RMI_S2AP_INDIRECT && rmm.static.rtt_s2ap_indirect == FEATURE_FALSE) then return FALSE; end; if (params.num_aux_planes > 0) then if (params.flags1.rtt_tree_per_plane == RMI_FEATURE_FALSE && rmm.static.rtt_plane == RTT_PLANE_AUX) then return FALSE; end; if (params.flags1.rtt_tree_per_plane == RMI_FEATURE_TRUE && rmm.static.rtt_plane == RTT_PLANE_SINGLE) then return FALSE; end; if ((params.flags1.rtt_tree_per_plane == RMI_FEATURE_TRUE && params.flags1.rtt_s2ap_encoding != RMI_S2AP_DIRECT) || (params.flags1.rtt_tree_per_plane == RMI_FEATURE_FALSE && params.flags1.rtt_s2ap_encoding != RMI_S2AP_INDIRECT )) then return FALSE; end; end; return TRUE; end;
```

## See also:

- [A2.2.6 Realm parameters](rmm-A2.2.md#a226-realm-parameters)
- [Chapter A3 Feature discovery and configuration](rmm-A3.md)

## B3.102 RealmRttBaseEqual function

Returns TRUE if RTT base values of realm match the provided values.

```
pure func RealmRttBaseEqual( realm : RmmRealm, rtt_base : Address, aux_rtt_base : array [[3]] of Address) => begin if (realm.rtt_base[[0]] != rtt_base) then
```

```
boolean return FALSE;
```

Chapter B3. Command condition functions B3.103. RecAt function

```
end; for i = 0 to 2 do if (realm.rtt_base[[i + 1]] != aux_rtt_base[[i]]) then return FALSE; end; end; return TRUE; end;
```

## B3.103 RecAt function

Returns the REC object located at physical address addr .

```
readonly func RecAt( addr : Address) =>
```

```
RmmRec
```

## See also:

- [A2.4 Realm Execution Context](rmm-A2.4.md)

## B3.104 RecAuxCount function

Returns the number of auxiliary Granules required for a REC in the Realm described by rd .

The return value is IMPLEMENTATION DEFINED based on the attributes of the Realm.

The return value is guaranteed not to be greater than 16.

For a given Realm, this function always returns the same value.

```
readonly impdef func rd : Address) => integer
```

## B3.105 RecDevMemResponseToRsi function

RecAuxCount(

Returns response to VDEV mapping validation request.

```
readonly func RecDevMemResponseToRsi( rec : RmmRec) => RsiResponse begin if ((rec.dev_mem_addr != rec.dev_mem_top) && (rec.dev_mem_response == RESPONSE_REJECT)) return RSI_RESPONSE_REJECT; end; return RSI_RESPONSE_ACCEPT; end;
```

## B3.106 RecFromMpidr function

Returns the REC object identified by the specified MPIDR value, in the current Realm.

```
readonly func RecFromMpidr( mpidr : bits(64)) =>
```

```
RmmRec
```

```
then
```

## B3.107 RecIndex function

Returns the REC index which corresponds to mpidr .

```
pure func RecIndex( mpidr : RmiRecMpidr) => integer begin return (UInt(mpidr.aff0) + 16 * UInt(mpidr.aff1) + 16 * 256 * UInt(mpidr.aff2) + 16 * 256 * 256 * UInt(mpidr.aff3)); end;
```

See also:

- [A2.4.3 REC index and MPIDR value](rmm-A2.4.md#a243-rec-index-and-mpidr-value)

## B3.108 RecRipasResponseToRsi function

Returns response to RIPAS change request.

- readonly func RecRipasResponseToRsi( rec : RmmRec) =&gt; RsiResponse begin if ((rec.ripas\_value == RIPAS\_RAM) &amp;&amp; (rec.ripas\_addr != rec.ripas\_top) &amp;&amp; (rec.ripas\_response == RESPONSE\_REJECT)) then return RSI\_RESPONSE\_REJECT; end; return RSI\_RESPONSE\_ACCEPT; end; See also: · A5.4 RIPAS change

## B3.109 RecS2APResponseToRsi function

Returns response to S2AP change request.

```
readonly func RecS2APResponseToRsi( rec : RmmRec) => RsiResponse begin if ((rec.s2ap_addr != rec.s2ap_top) && (rec.s2ap_response == RESPONSE_REJECT)) then return RSI_RESPONSE_REJECT; end; return RSI_RESPONSE_ACCEPT; end;
```

## See also:

- [A10.3.2.3 Stage 2 Access Permissions change within a multi-Plane Realm](rmm-A10.3.md#a10323-stage-2-access-permissions-change-within-a-multi-plane-realm)

## B3.110 RemExtend function

Extend a REM.

B3.111. RimExtendData function

The input to the hash function is constructed by concatenating the following, to form a 1024-bit value:

- old\_value
- The least significant size bits from new\_value
- 512 -size zero bits

This value is hashed using the algorithm identified by hash\_algo .

```
readonly func RemExtend( hash_algo : RmmHashAlgorithm, old_value : RmmRealmMeasurement, new_value : RmmRealmMeasurement, size : integer) =>
```

## See also:

- [A7.1.2 Realm Extensible Measurement](rmm-A7.1.md#a712-realm-extensible-measurement)

## B3.111 RimExtendData function

Extend RIM with contribution from DATA creation.

```
readonly func RimExtendData( realm : RmmRealm, ipa : Address, data : Address, flags : RmiDataFlags) =>
```

See also:

- B4.5.66.4 RMI\_RTT\_DATA\_MAP\_INIT extension of RIM

## B3.112 RimExtendRec function

Extend RIM with contribution from REC creation.

```
readonly func RimExtendRec( realm : RmmRealm, params : RmiRecParams) =>
```

See also:

- [B4.5.49.4 RMI\_REC\_CREATE extension of RIM](rmm-B4.5.49.md#b45494-rmi_rec_create-extension-of-rim)

## B3.113 RipasToRmi function

Encodes a RIPAS value.

```
readonly func RipasToRmi( ripas : RmmRipas) => RmiRipas begin case ripas of when RIPAS_EMPTY => return RMI_RIPAS_EMPTY; when RIPAS_RAM => return RMI_RIPAS_RAM; when RIPAS_DESTROYED => return RMI_RIPAS_DESTROYED; when RIPAS_DEV => return RMI_RIPAS_DEV; end; end;
```

```
RmmRealmMeasurement
```

```
RmmRealmMeasurement
```

```
RmmRealmMeasurement
```

## B3.114 RmiAddrBlockSizeToLevel function

## Decode an RMI Address Block Size.

```
readonly func RmiAddrBlockSizeToLevel( size : RmiAddrBlockSize) => integer begin case size of when RMI_BLOCK_L0 => return 0; when RMI_BLOCK_L1 => return 1; when RMI_BLOCK_L2 => return 2; when RMI_PAGE_L3 => return 3; otherwise => unreachable; end; end;
```

## B3.115 RmiAddrRangeDescDecode function

## Decode an RMI Address Range Descriptor.

```
RttLevelSize(level))
```

```
readonly func RmiAddrRangeDescDecode( desc : RmiAddrRangeDesc) => RmmAddrRange begin var rmm : RmmGlobal = Rmm(); var base : integer; var count : integer; var level : integer; case rmm.dynamic.rmi_granule_size of when 4 * KB => base = UInt(desc.data.granule_4kb.addr); count = desc.data.granule_4kb.count; level = RmiAddrBlockSizeToLevel( desc.data.granule_4kb.size); when 16 * KB => base = UInt(desc.data.granule_16kb.addr); count = desc.data.granule_16kb.count; level = RmiAddrBlockSizeToLevel( desc.data.granule_16kb.size); when 64 * KB => base = UInt(desc.data.granule_64kb.addr); count = desc.data.granule_64kb.count; level = RmiAddrBlockSizeToLevel( desc.data.granule_64kb.size); otherwise => unreachable; end; return RmmAddrRange { base = ToAddress(base), top = ToAddress(base + count * }; end;
```

## B3.116 RmiAddrRangesEqual function

Returns TRUE if two address ranges are equal.

```
then
```

```
pure func RmiAddrRangesEqual( range1 : RmmAddrRange, range2 : RmiAddrRange) => boolean begin if range1.base != range2.base return FALSE; end; if range1.top != range2.top then return FALSE; end; return TRUE; end;
```

## B3.117 RmiAddrRangesEqual16 function

Returns TRUE if the first count entries in two arrays of address ranges are equal.

```
then
```

```
pure func RmiAddrRangesEqual16( ranges1 : array [[16]] of RmmAddrRange, ranges2 : array [[16]] of RmiAddrRange, count : integer) => boolean begin assert 0 <= count && count <= 16; for i = 0 to count -1 do if ranges1[[i]].base != ranges2[[i]].base return FALSE; end; if ranges1[[i]].top != ranges2[[i]].top then return FALSE; end; end; return TRUE; end;
```

## B3.118 RmiAddrRangesEqual8 function

Returns TRUE if the first count entries in two arrays of address ranges are equal.

```
then
```

```
pure func RmiAddrRangesEqual8( ranges1 : array [[8]] of RmmAddrRange, ranges2 : array [[8]] of RmiAddrRange, count : integer) => boolean begin assert 0 <= count && count <= 8; for i = 0 to count -1 do if ranges1[[i]].base != ranges2[[i]].base return FALSE; end; if ranges1[[i]].top != ranges2[[i]].top then return FALSE; end; end; return TRUE; end;
```

## B3.119 RmiAddrRangesValid8 function

Returns TRUE if address ranges are sorted and non-overlapping.

```
readonly func RmiAddrRangesValid8( addr_range : array [[8]] of RmiAddrRange, num_addr_range : integer) => boolean begin var last_top : Address = ARBITRARY : Address; for i = 0 to num_addr_range -1 do var range : RmiAddrRange = addr_range[[i]]; if UInt(range.base) >= UInt(range.top) then return FALSE; end; if i > 0 && UInt(range.base) < UInt(last_top) return FALSE; end; last_top = range.top; end; return TRUE; end;
```

```
then
```

## B3.120 RmiCmemFlagsSupported function

Returns TRUE if the provided CMEM flags are supported by the implementation.

```
readonly impdef func flags : RmiCmemFlags) => boolean
```

## B3.121 RmiCmemParamsAt function

Returns CMEM parameters stored at physical address addr .

If the PAS of addr is not NS, the return value is UNKNOWN.

RmiCmemFlagsSupported(

```
readonly func RmiCmemParamsAt( addr : Address) =>
```

```
RmiCmemParams
```

## B3.122 RmiCmemParamsIsValid function

Returns TRUE if the memory location contains a valid encoding of the RmiCmemParams type and all the following are true:

- The parameters are consistent with the CMEM invariants.

```
RmiCmemParamsIsValid(
```

```
readonly func addr : Address) => boolean
```

## See also:

- [A9.11.3 Coherent memory device invariants](rmm-A9.11.md#a9113-coherent-memory-device-invariants)

## B3.123 RmiCmemPdevParamsAt function

Returns CMEM\_PDEV parameters stored at physical address addr .

If the PAS of addr is not NS, the return value is UNKNOWN.

```
readonly func RmiCmemPdevParamsAt( addr : Address) =>
```

```
RmiCmemPdevParams
```

## B3.124 RmiDevCommComplete function

Device communication is complete.

```
boolean
```

```
readonly func RmiDevCommComplete( flags : RmiDevCommExitFlags) => begin return ( flags.req_cache == RMI_FALSE && flags.rsp_cache == RMI_FALSE && flags.req_send == RMI_FALSE && flags.rsp_wait == RMI_FALSE && flags.rsp_reset == RMI_FALSE); end;
```

## B3.125 RmiDevCommDataAt function

Returns device communication data structure stored at physical address addr .

If the PAS of addr is not NS, the return value is UNKNOWN.

```
readonly func RmiDevCommDataAt( addr : Address) =>
```

## B3.126 RmiFeatureRegister0Decode function

Decode RmiFeatureRegister0 value.

```
readonly func RmiFeatureRegister0Decode( value : bits(64)) =>
```

## B3.127 RmiFeatureRegisterEncode function

Encode feature register.

```
readonly func RmiFeatureRegisterEncode( index : integer) => bits(64) begin var rmm : RmmGlobal = Rmm(); var result : bits(64) = Zeros{64}(); if (index == 0) then var reg : RmiFeatureRegister0; reg.S2SZ = rmm.static.max_ipa_width; reg.LPA2 = FeatureToRmi(rmm.static.feat_lpa2); reg.SVE = FeatureToRmi(rmm.static.feat_sve); reg.SVE_VL = rmm.static.max_sve_vl; assert rmm.static.num_bps >= 2 && rmm.static.num_bps <= 2^6; reg.NUM_BPS = rmm.static.num_bps -1; assert rmm.static.num_wps >= 2 && rmm.static.num_wps <= 2^6; reg.NUM_WPS = rmm.static.num_wps -1;
```

RmiDevCommData RmiFeatureRegister0

```
reg.PMU = FeatureToRmi(rmm.static.feat_pmu); reg.PMU_NUM_CTRS = rmm.static.pmu_num_ctrs; // Omitted: encode reg into bits(64) value end; if (index == 1) then var reg : RmiFeatureRegister1; reg.RMI_GRAN_SZ_4KB = FeatureToRmi(rmm.static.rmi_granule_size_4kb); reg.RMI_GRAN_SZ_16KB = FeatureToRmi(rmm.static.rmi_granule_size_16kb); reg.RMI_GRAN_SZ_64KB = FeatureToRmi(rmm.static.rmi_granule_size_64kb); reg.HASH_SHA_256 = FeatureToRmi(rmm.static.feat_sha_256); reg.HASH_SHA_384 = FeatureToRmi(rmm.static.feat_sha_384); reg.HASH_SHA_512 = FeatureToRmi(rmm.static.feat_sha_512); reg.MAX_RECS_ORDER = rmm.static.max_recs_order; // Omitted: set reg.L0GPTSZ // Omitted: set reg.PPS // Omitted: encode reg into bits(64) value end; if (index == 2) then var reg : RmiFeatureRegister2; reg.DA = FeatureToRmi(rmm.static.feat_da); reg.DA_COH = FeatureToRmi(rmm.static.feat_da_coh); reg.P2P = FeatureToRmi(rmm.static.feat_p2p); reg.VSMMU = FeatureToRmi(rmm.static.feat_vsmmu); reg.ATS = FeatureToRmi(rmm.static.feat_ats); reg.CMEM_CXL = FeatureToRmi(rmm.static.feat_cmem_cxl); reg.NON_TEE_STREAM = FeatureToRmi(rmm.static.feat_non_tee_stream); reg.MAX_VDEVS_ORDER = rmm.static.max_vdevs_order; reg.VDEV_KROU = FeatureToRmi(rmm.static.feat_vdev_krou); reg.MAX_CMEM = rmm.static.max_cmem; reg.CMEM_TSE_REQ = FeatureToRmi(rmm.static.feat_cmem_tse_req); // Omitted: encode reg into bits(64) value end; if (index == 3) then var reg : RmiFeatureRegister3; reg.MAX_NUM_AUX_PLANES = rmm.static.max_num_aux_planes; case rmm.static.rtt_plane of when RTT_PLANE_AUX => reg.RTT_PLANE = RMI_RTT_PLANE_AUX; when RTT_PLANE_AUX_SINGLE => reg.RTT_PLANE = RMI_RTT_PLANE_AUX_SINGLE; when RTT_PLANE_SINGLE => reg.RTT_PLANE = RMI_RTT_PLANE_SINGLE; end; reg.RTT_S2AP_INDIRECT = FeatureToRmi(rmm.static.rtt_s2ap_indirect); // Omitted: encode reg into bits(64) value end;
```

Chapter B3. Command condition functions B3.128. RmiPdevFlagsDecode function

```
if (index == 4) then var reg : RmiFeatureRegister4; reg.MEC_COUNT = rmm.static.mec_count; // Omitted: encode reg into bits(64) value end; return result; end;
```

## B3.128 RmiPdevFlagsDecode function

Decode RmiPdevFlags value.

```
readonly func RmiPdevFlagsDecode( value : bits(64)) =>
```

```
RmiPdevFlags
```

## B3.129 RmiPdevFlagsSupported function

Returns TRUE if the provided PDEV flags are supported by the implementation.

```
readonly func RmiPdevFlagsSupported( flags : RmiPdevFlags) => boolean begin var rmm : RmmGlobal = Rmm(); if (rmm.static.feat_da != FEATURE_TRUE) then return FALSE; end; if (rmm.static.feat_p2p != FEATURE_TRUE && flags.p2p == RMI_FEATURE_TRUE) then return FALSE; end; // Omitted: IMPDEF check for whether the PDEV category is // supported. // Omitted: IMPDEF checks for whether the following flags // are supported: // -spdm return TRUE; end;
```

## See also:

- [A9.2.1 Physical device attributes](rmm-A9.2.md#a921-physical-device-attributes)

## B3.130 RmiPdevParamsAt function

Returns PDEV parameters stored at physical address addr .

If the PAS of addr is not NS, the return value is UNKNOWN.

```
readonly func RmiPdevParamsAt( addr : Address) =>
```

```
RmiPdevParams
```

## B3.131 RmiPdevParamsIsValid function

Returns TRUE if the memory location contains a valid encoding of the RmiPdevParams type and all the following are true:

- The device identifier is valid
- The device identifier is not equal to the device identifier of another PDEV

```
RmiPdevParamsIsValid(
```

```
readonly func addr : Address) => boolean
```

## B3.132 RmiPdevStreamParamsAt function

Returns PDEV stream parameters stored at physical address addr .

If the PAS of addr is not NS, the return value is UNKNOWN.

```
readonly func RmiPdevStreamParamsAt( addr : Address) =>
```

```
RmiPdevStreamParams
```

## B3.133 RmiPdevStreamParamsIsValid function

Returns TRUE if the memory location contains a valid encoding of the RmiPdevStreamParams type and all the following are true:

- The IDE stream identifier is valid
- The base and top of every address range is aligned to the size of a Granule
- Every address range falls within a memory range permitted by the system
- None of the address ranges overlaps another address range for either PDEV
- None of the address ranges overlaps an address range for another PDEV
- A connection between the specified PDEV(s) is supported by the implementation

```
RmiPdevStreamParamsIsValid(
```


```
readonly func addr : Address) => boolean
```

## B3.134 RmiPsmmuParamsAt function

Returns PSMMU parameters stored at physical address addr .

If the PAS of addr is not NS, the return value is UNKNOWN.

```
readonly func RmiPsmmuParamsAt( addr : Address) =>
```

```
RmiPsmmuParams
```

## B3.135 RmiPublicKeyParamsAt function

Returns public key parameters stored at physical address addr .

If the PAS of addr is not NS, the return value is UNKNOWN.

```
readonly func RmiPublicKeyParamsAt( addr : Address) =>
```

```
RmiPublicKeyParams
```

## B3.136 RmiRealmParamsAt function

Returns Realm parameters stored at physical address addr .

If the PAS of addr is not NS, the return value is UNKNOWN.

```
readonly func RmiRealmParamsAt( addr : Address) =>
```

See also:

- [A2.2.6 Realm parameters](rmm-A2.2.md#a226-realm-parameters)

## B3.137 RmiRealmParamsIsValid function

Returns TRUE if the memory location contains a valid encoding of the RmiRealmParams type.

```
RmiRealmParamsIsValid(
```

```
readonly func addr : Address) => boolean
```

## B3.138 RmiRecParamsAt function

Returns REC parameters stored at physical address addr .

If the PAS of addr is not NS, the return value is UNKNOWN.

```
readonly func RmiRecParamsAt(
```

```
addr : Address) => RmiRecParams
```

## B3.139 RmiRecRunAt function

Returns the RecRun object stored at physical address addr .

```
readonly func RmiRecRunAt( addr : Address) =>
```

## See also:

- [A4.2 REC entry](rmm-A4.2.md)
- [A4.3 REC exit](rmm-A4.3.md)

## B3.140 RmiRmmConfigAt function

RmiRecRun

Returns system configuration stored at physical address addr .

If the PAS of addr is not NS, the return value is UNKNOWN.

```
readonly func RmiRmmConfigAt( addr : Address) =>
```

```
RmiRmmConfig
```

## B3.141 RmiVdevFlagsDecode function

Decode RmiVdevFlags value.

```
pure func RmiVdevFlagsDecode( value : bits(64)) =>
```

```
RmiVdevFlags
```

## B3.142 RmiVdevMeasureParamsAt function

Returns device measurement parameters stored at physical address addr .

```
If the PAS of addr is not NS, the return value is UNKNOWN. readonly func RmiVdevMeasureParamsAt(
```

```
RmiRealmParams
```

```
addr : Address) => RmiVdevMeasureParams
```

## B3.143 RmiVdevParamsAt function

Returns VDEV parameters stored at physical address addr .

If the PAS of addr is not NS, the return value is UNKNOWN.

```
readonly func RmiVdevParamsAt( addr : Address) =>
```

```
RmiVdevParams
```

## B3.144 RmiVdevParamsIsValid function

Returns TRUE if the memory location contains a valid encoding of the RmiPdevParams type.

```
RmiVdevParamsIsValid(
```

```
readonly func addr : Address) => boolean
```

## B3.145 RmiVersionHigherIsSupported function

Returns TRUE if the RMM supports an RMI revision which is incompatible with and greater than version .

```
readonly func RmiVersionHigherIsSupported( version : RmiInterfaceVersion) =>
```

## See also:

- [Chapter B2 Interface versioning](rmm-B2.md)
- [B4.5.92 RMI\_VERSION command](rmm-B4.5.92.md)

## B3.146 RmiVersionHighest function

Returns the highest RMI revision supported by the RMM.

```
readonly func RmiVersionHighest() => RmiInterfaceVersion
```

## See also:

- [Chapter B2 Interface versioning](rmm-B2.md)
- [B4.5.92 RMI\_VERSION command](rmm-B4.5.92.md)

## B3.147 RmiVersionHighestBelow function

Returns the highest RMI revision which is both less than version and supported by the RMM.

```
readonly func RmiVersionHighestBelow( version : RmiInterfaceVersion) => RmiInterfaceVersion
```

## See also:

- [Chapter B2 Interface versioning](rmm-B2.md)
- [B4.5.92 RMI\_VERSION command](rmm-B4.5.92.md)

## B3.148 RmiVersionIsSupported function

Returns TRUE if the RMM supports an RMI revision which is compatible with version .

readonly func RmiVersionIsSupported(

boolean

```
version : RmiInterfaceVersion) => boolean
```

See also:

- [Chapter B2 Interface versioning](rmm-B2.md)
- [B4.5.92 RMI\_VERSION command](rmm-B4.5.92.md)

## B3.149 RmiVersionLowerIsSupported function

Returns TRUE if the RMM supports an RMI revision which is incompatible with and less than version .

```
readonly func RmiVersionLowerIsSupported( version : RmiInterfaceVersion) =>
```

See also:

- [Chapter B2 Interface versioning](rmm-B2.md)
- [B4.5.92 RMI\_VERSION command](rmm-B4.5.92.md)

## B3.150 RmiVsmmuParamsAt function

Returns VSMMU parameters stored at physical address addr .

If the PAS of addr is not NS, the return value is UNKNOWN.

```
readonly func RmiVsmmuParamsAt( addr : Address) =>
```

See also:

- [A9.8.3 VSMMU liveness](rmm-A9.8.md#a983-vsmmu-liveness)

## B3.151 RmiVsmmuParamsIsValid function

Returns TRUE if the memory location contains a valid encoding of the RmiVsmmuParams type and all the following are true:

RmiVsmmuParams

- aidr value is set to an architecturally valid value.
- aidr value does not define any features which are unsupported by the RMM.
- All idr[] values are set to an architecturally valid value.
- No idr[] value defines any features which are unsupported by the RMM.

Here, 'architecturally valid' refers to the SMMU implementation to which this VSMMU belongs.

```
readonly func RmiVsmmuParamsIsValid( addr : Address) => boolean
```

See also:

- Arm System Memory Management Unit Architecture Specification [22]
- [A9.8 Virtual SMMU](rmm-A9.8.md)

## B3.152 Rmm function

Returns global state of the implementation.

```
readonly impdef func Rmm() => RmmGlobal
```

See also:

```
boolean
```

- A2.1 RMM
- Chapter A3 Feature discovery and configuration

## B3.153 RmmConfigIsSupported function

System configuration is supported.

```
readonly func RmmConfigIsSupported( cfg : RmiRmmConfig) => boolean begin var rmm : RmmGlobal = Rmm(); case cfg.rmi_granule_size of when RMI_GRANULE_SIZE_4KB => if rmm.static.rmi_granule_size_4kb != FEATURE_TRUE then return FALSE; end; when RMI_GRANULE_SIZE_16KB => if rmm.static.rmi_granule_size_16kb != FEATURE_TRUE then return FALSE; end; when RMI_GRANULE_SIZE_64KB => if rmm.static.rmi_granule_size_64kb != FEATURE_TRUE then return FALSE; end; end; if (TrackingRegionSizeFromRmi( cfg.rmi_granule_size, cfg.tracking_region_size) == 0) then return FALSE; end; return TRUE; end;
```

## B3.154 RsiFeatureRegisterEncode function

## Encode feature register.

```
readonly func RsiFeatureRegisterEncode( realm : RmmRealm, index : integer) => bits(64) begin var result : bits(64) = Zeros{64}(); if (index == 0) then var reg : RsiFeatureRegister0; reg.DA = FeatureToRsi(realm.feat_da); // Omitted: set reg.MRO depending on whether platform // implements FEAT_S2PIE reg.ATS = FeatureToRsi(realm.feat_ats); // Omitted: encode reg into bits(64) value end;
```

Chapter B3. Command condition functions B3.155. RsiHostCallAt function

```
return result; end;
```

## B3.155 RsiHostCallAt function

Returns Host call data stored at IPA addr , mapped in the current Realm.

```
readonly func RsiHostCallAt( addr : Address) => RsiHostCall
```

## B3.156 RsiPlaneRunAt function

Returns the PlaneRun object stored at IPA addr .

```
readonly func RsiPlaneRunAt( realm : RmmRealm, addr : Address) =>
```

```
RsiPlaneRun
```

## B3.157 RsiRealmConfigAt function

Returns Realm configuration stored at IPA addr , mapped in the current Realm.

```
readonly func RsiRealmConfigAt( addr : Address) => RsiRealmConfig
```

## B3.158 RsiRealmMeasurement function

Realm measurement value.

```
readonly func RsiRealmMeasurement( realm : RmmRealm, index : integer) => begin if (index == 0) then return realm.rim; end; assert 1 <= index && index <= 4; return realm.rem[[index -1]]; end;
```

```
RmmRealmMeasurement
```

## B3.159 RsiVdevInfoAt function

Returns device configuration stored at IPA addr , mapped in the current Realm.

```
readonly func RsiVdevInfoAt( addr : Address) =>
```

```
RsiVdevInfo
```

## B3.160 RsiVersionHigherIsSupported function

Returns TRUE if the RMM supports an RSI revision which is incompatible with and greater than version .

```
readonly func RsiVersionHigherIsSupported( version : RsiInterfaceVersion) =>
```

See also:

- [Chapter B2 Interface versioning](rmm-B2.md)

```
boolean
```

B3.161. RsiVersionHighest function

- B5.4.22 RSI\_VERSION command

## B3.161 RsiVersionHighest function

Returns the highest RSI revision supported by the RMM.

```
readonly func RsiVersionHighest() => RsiInterfaceVersion
```

## See also:

- [Chapter B2 Interface versioning](rmm-B2.md)
- [B5.4.22 RSI\_VERSION command](rmm-B5.4.22.md)

## B3.162 RsiVersionHighestBelow function

Returns the highest RSI revision which is both less than version and supported by the RMM.

```
readonly func RsiVersionHighestBelow( version : RsiInterfaceVersion) =>
```

## See also:

- [Chapter B2 Interface versioning](rmm-B2.md)
- [B5.4.22 RSI\_VERSION command](rmm-B5.4.22.md)

## B3.163 RsiVersionIsSupported function

Returns TRUE if the RMM supports an RSI revision which is compatible with version .

```
readonly func RsiVersionIsSupported( version : RsiInterfaceVersion) =>
```

## See also:

- [Chapter B2 Interface versioning](rmm-B2.md)
- [B5.4.22 RSI\_VERSION command](rmm-B5.4.22.md)

```
RsiInterfaceVersion
```

boolean

## B3.164 RsiVersionLowerIsSupported function

Returns TRUE if the RMM supports an RSI revision which is incompatible with and less than version .

```
readonly func RsiVersionLowerIsSupported(
```

```
version : RsiInterfaceVersion) => boolean
```

## See also:

- [Chapter B2 Interface versioning](rmm-B2.md)
- [B5.4.22 RSI\_VERSION command](rmm-B5.4.22.md)

## B3.165 RttAllEntriesContiguous function

Returns TRUE if all entries in the RTT at address rtt at level level have contiguous output addresses, starting with addr .

```
RttAllEntriesContiguous(
```

```
readonly func rtt : RmmRtt, addr : Address, level : integer) => boolean
```

See also:

- [A5.6 Realm Translation Table](rmm-A5.6.md)

## B3.166 RttAllEntriesMemAttr function

Returns TRUE if the memory attributes of all entries in the RTT at address rtt are equal to the memory attributes in rtte .

```
readonly func RttAllEntriesMemAttr( rtt : RmmRtt, rtte : RmmRttEntry) => boolean
```

## B3.167 RttAllEntriesRipas function

Returns TRUE if all entries in the RTT at address rtt have RIPAS ripas .

```
readonly func RttAllEntriesRipas( rtt : RmmRtt, ripas : RmmRipas) => boolean
```

## B3.168 RttAllEntriesS2AP function

Returns TRUE if the S2AP of all entries in the RTT at address rtt are equal to the S2AP in rtte .

```
readonly func RttAllEntriesS2AP( rtt : RmmRtt, rtte : RmmRttEntry) =>
```

## B3.169 RttAllEntriesState function

Returns TRUE if all entries in the RTT at address rtt have state state .

```
readonly func RttAllEntriesState( rtt : RmmRtt, state : RmmRttEntryState) =>
```

See also:

- [A5.6 Realm Translation Table](rmm-A5.6.md)

## B3.170 RttAt function

Returns the RTT at address rtt .

```
readonly func RttAt( addr : Address) => RmmRtt
```

## B3.171 RttConfigIsValid function

Returns TRUE if the RTT configuration values provided are self-consistent and are supported by the platform.

```
readonly func RttConfigIsValid( ipa_width : integer, rtt_level_start : integer, rtt_num_start : integer) =>
```

See also:

```
boolean
```

```
boolean
```

```
boolean
```

- A5.6 Realm Translation Table

## B3.172 RttDescriptorDecode function

Decode an RTT descriptor.

```
pure func RttDescriptorDecode( desc : bits(64), encoding : RmmRttS2APEncoding) =>
```

```
RmmRttEntry
```

## B3.173 RttDescriptorIsValidForUnprotected function

Returns TRUE if, within the descriptor desc , all of the following are true:

- All fields which are Host-controlled Unprotected RTT attributes are set to architecturally valid values.
- All fields which are not Host-controlled Unprotected RTT attributes are set to zero.

```
RttDescriptorIsValidForUnprotected(
```

```
pure func desc : bits(64)) => boolean
```

## See also:

Returns TRUE if all entries in the RTT at address rtt at level level , within Protected IPA range [base, top), have output addresses which map to coherent device memory.

## · A5.6.12.3 Memory attributes for RTTE\_MAPPED\_NS mappings B3.174 RttEntriesInRangeCohDevMem function readonly func RttEntriesInRangeCohDevMem( rtt : RmmRtt, level : integer, base : Address, top : Address) =&gt; boolean begin var addr : Address = base; var size : integer = RttLevelSize(level); while (UInt(addr) &lt; UInt(top)) do var index : integer = RttEntryIndex(addr, level); var rtte : RmmRttEntry = RttEntryAt(rtt, index); if (!PaIsDelegableCohDevMem(rtte.addr)) then return FALSE; end; addr = ToAddress(UInt(addr) + size); end; return TRUE; end;

## B3.175 RttEntriesInRangeMemAttr function

Returns TRUE if all entries in the RTT at address rtt at level level , within Protected IPA range [base, top), have memory attributes attr .

readonly func RttEntriesInRangeMemAttr(

```
rtt : RmmRtt, level : integer, base : Address, top : Address, attr : RmmRttMemAttr) => boolean begin var addr : Address = base; var size : integer = RttLevelSize(level); while (UInt(addr) < UInt(top)) do var index : integer = RttEntryIndex(addr, level); var rtte : RmmRttEntry = RttEntryAt(rtt, index); if (rtte.attr_prot != attr) then return FALSE; end; addr = ToAddress(UInt(addr) + size); end; return TRUE; end;
```

## B3.176 RttEntriesInRangeNonCohDevMem function

Returns TRUE if all entries in the RTT at address rtt at level level , within Protected IPA range [base, top), have output addresses which map to non-coherent device memory.

```
readonly func RttEntriesInRangeNonCohDevMem( rtt : RmmRtt, level : integer, base : Address, top : Address) => boolean begin var addr : Address = base; var size : integer = RttLevelSize(level); while (UInt(addr) < UInt(top)) do var index : integer = RttEntryIndex(addr, var rtte : RmmRttEntry = RttEntryAt(rtt, index); if (!PaIsDelegableNonCohDevMem(rtte.addr)) then return FALSE; end; addr = ToAddress(UInt(addr) + size); end; return TRUE; end;
```

```
level);
```

## B3.177 RttEntriesInRangeOutputContiguous function

Returns TRUE if all entries in the RTT at address rtt at level level , within IPA range [base, top), map to a contiguous range of output addresses starting from out .

```
readonly func RttEntriesInRangeOutputContiguous( rtt : RmmRtt, level : integer,
```

```
base : Address, top : Address, out : Address) => boolean begin var in_addr : Address = base; var out_addr : Address = out; var size : integer = RttLevelSize(level); while (UInt(in_addr) < UInt(top)) do var index : integer = RttEntryIndex(in_addr, level); var rtte : RmmRttEntry = RttEntryAt(rtt, index); if (rtte.addr != out_addr) then return FALSE; end; in_addr = ToAddress(UInt(in_addr) + size); out_addr = ToAddress(UInt(out_addr) + size); end; return TRUE; end;
```

## B3.178 RttEntriesInRangeRipas function

Returns TRUE if all entries in the RTT at address rtt at level level , within IPA range [base, top), have RIPAS ripas .

```
readonly func RttEntriesInRangeRipas( rtt : RmmRtt, level : integer, base : Address, top : Address, ripas : RmmRipas) => boolean begin var addr : Address = base; var size : integer = RttLevelSize(level); while (UInt(addr) < UInt(top)) do var index : integer = RttEntryIndex(addr, var rtte : RmmRttEntry = RttEntryAt(rtt, index); if (rtte.ripas != ripas) then return FALSE; end; addr = ToAddress(UInt(addr) + size); end; return TRUE; end;
```

```
level);
```

## B3.179 RttEntryAt function

Returns the i th entry in the RTT rtt .

```
readonly func RttEntryAt( rtt : RmmRtt, i : integer) =>
```

```
RmmRttEntry
```

Chapter B3. Command condition functions

## See also:

- [A5.6 Realm Translation Table](rmm-A5.6.md)

## B3.180 RttEntryIndex function

Returns the index of the entry in a level level RTT which is identified by addr .

```
readonly func RttEntryIndex( addr : Address, level : integer) =>
```

## See also:

- [A5.6 Realm Translation Table](rmm-A5.6.md)

## B3.181 RttEntryStateToRmi function

Encodes the state of an RTTE.

```
readonly func RttEntryStateToRmi( state : RmmRttEntryState) => RmiRttEntryState begin case state of when RTTE_VOID => return RMI_RTTE_VOID; when RTTE_DATA => return RMI_RTTE_DATA; when RTTE_UNMAPPED_NS => return RMI_RTTE_VOID; when RTTE_MAPPED_NS => return RMI_RTTE_DATA; when RTTE_TABLE => return RMI_RTTE_TABLE; when RTTE_NARCH_DEV => return RMI_RTTE_NARCH_DEV; when RTTE_AUX_DESTROYED => return RMI_RTTE_AUX_DESTROYED; when RTTE_ARCH_DEV => return RMI_RTTE_ARCH_DEV; end; end;
```

## B3.182 RttFold function

Returns the RTTE which results from folding the homogeneous RTT at address rtt .

```
pure func RttFold( rtt : RmmRtt) =>
```

## See also:

- [A5.6.6 RTT folding](rmm-A5.6.md#a566-rtt-folding)

## B3.183 RttIsHomogeneous function

Returns TRUE if the RTT at address rtt is homogeneous.

```
pure func RttIsHomogeneous( rtt : RmmRtt) => boolean
```

## See also:

- [A5.6.6 RTT folding](rmm-A5.6.md#a566-rtt-folding)

```
RmmRttEntry
```

```
integer
```

Chapter B3. Command condition functions

## B3.184 RttIsLive function

Returns TRUE if the RTT at address rtt is live.

```
pure func RttIsLive( rtt : RmmRtt) =>
```

```
boolean
```

## See also:

- [A5.6.8 RTTE liveness and RTT liveness](rmm-A5.6.md#a568-rtte-liveness-and-rtt-liveness)
- [A5.6.9 RTT destruction](rmm-A5.6.md#a569-rtt-destruction)

## B3.185 RttLevelIsStarting function

Returns TRUE if level is the starting level of the RTT for the Realm described by rd .

```
pure func RttLevelIsStarting( realm : RmmRealm, level : integer) =>
```

## See also:

- [A5.6 Realm Translation Table](rmm-A5.6.md)

## B3.186 RttLevelIsValid function

Returns TRUE if level is a valid RTT level for the Realm described by rd .

```
pure func RttLevelIsValid( realm : RmmRealm, level : integer) =>
```

## See also:

- [A5.6 Realm Translation Table](rmm-A5.6.md)

## B3.187 RttLevelSize function

```
boolean
```

```
boolean
```

Returns the size of the address space described by each entry in an RTT at level.

If level is invalid, the return value is UNKNOWN.

```
readonly func RttLevelSize( level : integer) =>
```

## See also:

- [A5.6 Realm Translation Table](rmm-A5.6.md)

## B3.188 RttMemAttrEqual function

Returns TRUE if the memory attributes of the two RTT entries match.

```
readonly func RttMemAttrEqual( rtte1 : RmmRttEntry, rtte2 : RmmRttEntry, prot : RmmRttProtected) => boolean begin case prot of
```

```
integer
```

Chapter B3. Command condition functions B3.189. RttS2APEqual function

```
when RTT_PROTECTED => return rtte1.attr_prot == rtte2.attr_prot; when RTT_UNPROTECTED => return rtte1.attr_unprot == rtte2.attr_unprot; end; end;
```

## B3.189 RttS2APEqual function

Returns TRUE if the S2AP of the two RTT entries match.

```
readonly func RttS2APEqual( rtte1 : RmmRttEntry, rtte2 : RmmRttEntry, encoding : RmmRttS2APEncoding) => boolean begin case encoding of when S2AP_DIRECT => return ( (rtte1.s2ap_direct.read == rtte2.s2ap_direct.read) && (rtte1.s2ap_direct.write == rtte2.s2ap_direct.write)); when S2AP_INDIRECT => return ( (rtte1.s2ap_indirect.base_index == rtte2.s2ap_indirect.base_index) && (rtte1.s2ap_indirect.overlay_index == end; end;
```

## B3.190 RttsAllProtectedEntriesRipas function

Returns TRUE if the RIPAS of all entries identified by Protected IPAs in all of the starting-level RTT Granules is equal to ripas .

```
readonly func rtt_base : Address, rtt_num_start : integer, ripas : RmmRipas) => boolean
```

```
rtte2.s2ap_indirect.overlay_index)); RttsAllProtectedEntriesRipas(
```

## B3.191 RttsAllProtectedEntriesState function

Returns TRUE if the state of all entries identified by Protected IPAs in all of the starting-level RTT Granules is equal to state .

```
readonly func RttsAllProtectedEntriesState( rtt_base : Address, rtt_num_start : integer, state : RmmRttEntryState) => boolean
```

## B3.192 RttsAllUnprotectedEntriesState function

Returns TRUE if the state of all entries identified by Unprotected IPAs in all of the starting-level RTT Granules is equal to state .

```
readonly func RttsAllUnprotectedEntriesState( rtt_base : Address, rtt_num_start : integer,
```

```
state : RmmRttEntryState) => boolean
```

## B3.193 RttsGranuleState function

Inductive function which identifies the states of the starting-level RTT Granules.

This function is used in the definition of command footprint.

```
readonly func RttsGranuleState( rtt_base : Address, rtt_num_start : integer)
```

## B3.194 RttSkipEntriesIfState function

Scanning rtt starting from base , returns the IPA of the first entry whose state is state .

If no entry is found whose state is state , returns the next IPA after the last entry in rtt .

The return value is aligned to the size of the address range described by an entry at RTT level .

```
readonly func RttSkipEntriesIfState( rtt : RmmRtt, level : integer, base : Address, state : RmmRttEntryState) =>
```

## B3.195 RttSkipEntriesUnlessRipas function

Scanning rtt starting from ipa , returns the IPA of the first entry whose RIPAS is ripas .

If no entry is found whose RIPAS is ripas , returns the next IPA after the last entry in rtt .

The return value is aligned to the size of the address range described by an entry at RTT level .

```
readonly func rtt : RmmRtt, level : integer, ipa : Address, ripas : RmmRipas) => Address
```

```
Address RttSkipEntriesUnlessRipas(
```

## B3.196 RttSkipEntriesUnlessState function

Scanning rtt starting from ipa , returns the IPA of the first entry whose state is state .

If no entry is found whose state is state , returns the next IPA after the last entry in rtt .

The return value is aligned to the size of the address range described by an entry at RTT level .

```
readonly func rtt : RmmRtt, level : integer, ipa : Address, state : RmmRttEntryState) =>
```

```
RttSkipEntriesUnlessState( Address
```

## B3.197 RttSkipEntriesUnlessVoidOrData function

Scan rtt starting from base and terminating at top .

Return IPA of the first entry whose state is neither RTTE\_VOID nor RTTE\_DATA.

readonly func RttSkipEntriesUnlessVoidOrData(

```
rtt : RmmRtt, level : integer, base : Address, top : Address) => Address begin var top_void : Address = RttSkipEntriesIfState( rtt, level, base, RTTE_VOID); var top_data : Address = RttSkipEntriesIfState( rtt, level, base, RTTE_DATA); return MinAddress( MinAddress(top_void, top_data), top); end;
```

## B3.198 RttSkipEntriesWithRipas function

Scan rtt starting from base and terminating at top .

- If stop\_at\_destroyed is FALSE then return IPA of the first entry whose state is RTTE\_TABLE.
- If stop\_at\_destroyed is TRUE then return IPA of the first entry whose state is RTTE\_TABLE or whose RIPAS is RIPAS\_DESTROYED.

If no such entry is found, returns the smaller of:

- The next IPA after the last entry in rtt
- The top argument.

The return value is aligned to the size of the address range described by an entry at RTT level .

```
readonly func RttSkipEntriesWithRipas( rtt : RmmRtt, level : integer, base : Address, top : Address, stop_at_destroyed : boolean) => Address begin var result : Address = rtt, level, base, RTTE_TABLE); if stop_at_destroyed then result = MinAddress(result, RttSkipEntriesUnlessRipas( rtt, level, base, RIPAS_DESTROYED)); end; result = MinAddress(result, top); return AlignDownToRttLevel(result, level); end;
```

```
RttSkipEntriesUnlessState(
```

## B3.199 RttSkipNonLiveEntries function

Scanning rtt starting from ipa , returns the IPA of the first live entry.

If no live entry is found, returns the next IPA after the last entry in rtt .

The return value is aligned to the size of the address range described by an entry at RTT level .

```
readonly func RttSkipNonLiveEntries( rtt : RmmRtt, level : integer, ipa : Address) => Address begin var result : Address = RttSkipEntriesUnlessState( rtt, level, ipa, RTTE_DATA); result = MinAddress(result, RttSkipEntriesUnlessState( rtt, level, ipa, RTTE_MAPPED_NS)); result = MinAddress(result, RttSkipEntriesUnlessState( rtt, level, ipa, RTTE_TABLE)); result = MinAddress(result, RttSkipEntriesUnlessState( rtt, level, ipa, RTTE_NARCH_DEV)); return AlignDownToRttLevel(result, level); end;
```

## B3.200 RttsStateEqual function

See also: · A5.6.8 RTTE liveness and RTT liveness Returns TRUE if the state of all of the starting-level RTT Granules is equal to state . readonly func RttsStateEqual( rtt\_base : Address, rtt\_num\_start : integer, state : RmmGranuleState) =&gt; boolean begin var rmm : RmmGlobal = Rmm(); for i = 0 to rtt\_num\_start -1 do var addr = (UInt(rtt\_base) + i * rmm.dynamic.rmi\_granule\_size)[(ADDRESS\_WIDTH-1):0]; if (!PaIsTracked(addr) || GranuleAt(addr).state != state) then return FALSE; end; end; return TRUE; end;

## B3.201 RttTreeRangeAllMemAttr function

Returns TRUE if all RTT entries for RTT tree tree in Realm realm within IPA range [base, top) have memory attributes equal to memattr .

If the argument is a bits(3) then it is encoded as for MemAttr[2:0] in a translation table page or block descriptor.

```
readonly func RttTreeRangeAllMemAttr( realm : RmmRealm, tree : integer,
```

Chapter B3.

Command condition functions

B3.202.

RttTreeRangeAllMemAttrEqual function

```
base : Address, top : Address, memattr : RmmRttMemAttr) => boolean
```

```
readonly func RttTreeRangeAllMemAttr( realm : RmmRealm, tree : integer, base : Address, top : Address, memattr : bits(3)) => boolean
```

## B3.202 RttTreeRangeAllMemAttrEqual function

Returns TRUE if RTT entries in Realm realm within IPA range [base, top) have the same memory attributes in RTT trees tree\_1 and tree\_2 .

```
RttTreeRangeAllMemAttrEqual(
```

```
readonly func realm : RmmRealm, tree_1 : integer, tree_2 : integer, base : Address, top : Address) => boolean
```

## B3.203 RttTreeRangeAllOaddr function

Returns TRUE if all RTT entries for RTT tree tree in Realm realm within IPA range [base, top) have output address equal to addr .

```
readonly func realm : RmmRealm, tree : integer, base : Address, top : Address, addr : Address) => boolean
```

## B3.204 RttTreeRangeAllOaddrContig function

```
RttTreeRangeAllOaddr(
```

Returns TRUE if RTT entries for RTT tree tree in Realm realm within IPA range [base, top) have output addresses which map linearly to PA range [obase, obase + size).

```
RttTreeRangeAllOaddrContig(
```

```
readonly func realm : RmmRealm, tree : integer, ibase : Address, obase : Address, size : integer) => boolean
```

## B3.205 RttTreeRangeAllOaddrEqual function

Returns TRUE if RTT entries in Realm realm within IPA range [base, top) have the same output addresses in RTT trees tree\_1 and tree\_2 .

```
RttTreeRangeAllOaddrEqual(
```

```
readonly func realm : RmmRealm, tree_1 : integer, tree_2 : integer, base : Address, top : Address) => boolean
```

## B3.206 RttTreeRangeAllOaddrList function

Returns TRUE if RTT entries for RTT tree tree in Realm realm within IPA range [base, top) have output addresses which map linearly to the first size bytes of the address set described by an RMI Address List stored at PA alist .

```
RttTreeRangeAllOaddrList(
```

```
readonly func realm : RmmRealm, tree : integer, ibase : Address, alist : Address, size : integer) => boolean
```

## B3.207 RttTreeRangeAllS2AP function

Returns TRUE if all RTT entries for RTT tree tree in Realm realm within IPA range [base, top) have S2AP equal to s2ap .

If the Realm uses S2AP direct encoding, this is encoded as for AP in a translation table page or block descriptor.

If the Realm uses S2AP indirect encoding, this is encoded as for PIIndex in a translation table page or block descriptor.

```
readonly func realm : RmmRealm, tree : integer, base : Address, top : Address, s2ap : bits(4)) => boolean
```

## B3.208 RttTreeRangeAllShareability function

Returns TRUE if all RTT entries for RTT tree tree in Realm realm within IPA range [base, top) have shareability equal to shareability .

```
readonly func RttTreeRangeAllShareability( realm : RmmRealm, tree : integer, base : Address, top : Address, shareability : RmmRttShareability) =>
```

```
RttTreeRangeAllS2AP(
```

```
boolean
```

## B3.209 RttTreeRangeAllShareabilityEqual function

Returns TRUE if RTT entries in Realm realm within IPA range [base, top) have the same shareability in RTT trees tree\_1 and tree\_2 .

```
RttTreeRangeAllShareabilityEqual(
```

```
readonly func realm : RmmRealm, tree_1 : integer, tree_2 : integer, base : Address, top : Address) => boolean
```

## B3.210 RttTreeRangeAllState function

Returns TRUE if all RTT entries for RTT tree tree in Realm realm within IPA range [base, top) have state equal to state .

```
readonly func RttTreeRangeAllState( realm : RmmRealm, tree : integer, base : Address, top : Address, state : RmmRttEntryState) =>
```

## B3.211 RttWalk function

Returns the result of an RTT walk from the base of RTT tree tree owned by rd , to address addr .

The walk does not progress beyond level .

```
readonly func RttWalk( realm : RmmRealm, addr : Address, level : integer, tree : integer) =>
```

## See also:

- [A5.6.10 RTT walk](rmm-A5.6.md#a5610-rtt-walk)

## B3.212 RttWalkAnyNotAligned function

Performs one or more RTT walks within the IPA range [base, top) , on one or more RTT trees owned by rd .

For a Realm which is configured to use an RTT tree per Plane, it is permitted for an implementation to either walk just one of the RTTs, or to walk all of them.

It is permitted for an implementation to perform multiple walks, at successive IPAs, on the same RTT.

If one of the walks performed terminates earlier than level then the return value indicates the RTT index and the IPA at which the walk was performed. In this case, the result's 'valid' value is TRUE.

If none of the walks performed terminates earlier than level then the result's 'valid' value is FALSE.


```
readonly func RttWalkAnyNotAligned( realm : RmmRealm, base : Address, top : Address, level : integer) => RmmRttWalkNotAligned
```

## B3.213 TdiIdIsFree function

Returns TRUE if tdi\_id is unused within the namespace identified by routing\_id .

```
readonly func TdiIdIsFree( tdi_id : bits(64), routing_id : bits(64)) =>
```

## B3.214 ToAddress function

Convert integer to Address.

```
readonly func ToAddress(value : integer) => begin return value[(ADDRESS_WIDTH-1):0]; end;
```

```
boolean
```

```
RmmRttWalkResult
```

```
boolean
```

```
Address
```

Chapter B3. Command condition functions

## B3.215 ToBits64 function

Convert integer to Bits64.

```
pure func ToBits64(value : integer) => bits(64) begin return value[63:0]; end;
```

## B3.216 TrackingRegionAt function

Returns tracking region whose base address is addr .

```
readonly func TrackingRegionAt( addr : Address) =>
```

```
RmmTrackingRegion
```

## B3.217 TrackingRegionGranularity function

Returns granularity at which specified region is tracked.

```
readonly func TrackingRegionGranularity( region : RmmTrackingRegion) => integer begin var rmm : RmmGlobal = Rmm(); assert TrackingRegionIsTracked(region); case region.state of when TRACKING_COARSE => return rmm.dynamic.tracking_region_size; when TRACKING_FINE => return rmm.dynamic.rmi_granule_size; end; end;
```

## B3.218 TrackingRegionIsTracked function

Returns TRUE if the tracking region is tracked.

```
```

```
boolean
```

```
readonly func TrackingRegionIsTracked( region : RmmTrackingRegion) => begin return region.state IN { TRACKING_COARSE, TRACKING_FINE }; end;
```

## B3.219 TrackingRegionSizeFromRmi function

Decodes a tracking region size.

```
readonly func TrackingRegionSizeFromRmi( granule_size : RmiGranuleSize, tracking_region_size : integer) => integer begin case granule_size of when RMI_GRANULE_SIZE_4KB => case tracking_region_size of when 0 => return 1 GB; // Level 1 block
```

```
* size
```

```
otherwise => return 0; end; when RMI_GRANULE_SIZE_16KB => case tracking_region_size of when 0 => return 32 * MB; // Level 2 block size when 1 => return 64 * GB; // Level 1 block size otherwise => return 0; end; when RMI_GRANULE_SIZE_64KB => case tracking_region_size of when 0 => return 512 * MB; // Level 2 block size when 1 => return 4 * TB; // Level 1 block size otherwise => return 0; end; end; end;
```

## B3.220 TrackingRegionSizeToRmi function

```
Encodes a block size. readonly func TrackingRegionSizeToRmi( granule_size : integer, tracking_region_size : integer) => integer begin case granule_size of when 4 * KB => case tracking_region_size of when 1 * GB => return 0; // Level 1 block size otherwise => unreachable; end; when 16 * KB => case tracking_region_size of when 32 * MB => return 0; // Level 2 block size when 64 * GB => return 1; // Level 1 block size otherwise => unreachable; end; when 64 * KB => case tracking_region_size of when 512 * MB => return 0; // Level 2 block size when 4 * TB => return 1; // Level 1 block size otherwise => unreachable; end; end; end;
```

## B3.221 VdevAddrInRange function

Returns TRUE if addr is within the address ranges of vdev .

```
readonly func VdevAddrInRange( addr : Address, vdev : RmmVdev) => boolean begin for i = 0 to vdev.num_addr_range -1 do
```

```
Chapter B3. Command condition functions B3.222. VdevAt function then
```

```
var range : RmmAddrRange = vdev.addr_range[[i]]; if AddrIsWithin(addr, range.base, range.top) return TRUE; end; end; return FALSE; end;
```

## B3.222 VdevAt function

Returns the VDEV object located at physical address addr .

```
readonly func VdevAt( addr : Address) =>
```

```
RmmVdev
```

## B3.223 VdevAttestInfoEqual function

Returns TRUE if the VDEV attestation info matches.

```
pure func VdevAttestInfoEqual( lock_nonce : integer, meas_nonce : integer, report_nonce : integer, attest_info : RmmVdevAttestInfo) => boolean begin return (lock_nonce == attest_info.lock_nonce && meas_nonce == attest_info.meas_nonce && report_nonce == attest_info.report_nonce); end; pure func VdevAttestInfoEqual( attest_info_1 : RmmVdevAttestInfo, attest_info_2 : RmmVdevAttestInfo) => boolean begin return (attest_info_1.lock_nonce == attest_info_2.lock_nonce && attest_info_1.meas_nonce == attest_info_2.meas_nonce && attest_info_1.report_nonce == attest_info_2.report_nonce); end;
```

## B3.224 VdevFindMapped function

Returns TRUE if any Granule within the address ranges of vdev is mapped.

```
readonly func VdevFindMapped( vdev : RmmVdev) => RmmVdevAddrResult begin var rmm : RmmGlobal = Rmm(); for i = 0 to vdev.num_addr_range -1 do var range : RmmAddrRange = vdev.addr_range[[i]]; var addr : Address = range.base; while UInt(addr) < UInt(range.top) do if GranuleAt(addr).state == GRAN_DEV then return RmmVdevAddrResult { valid = RMM_TRUE, addr = addr }; end; addr = ToAddress(UInt(addr) + rmm.dynamic.rmi_granule_size); end; end;
```

```
Chapter B3. Command condition functions
```

```
return RmmVdevAddrResult { valid = RMM_FALSE, addr = ARBITRARY : Address }; end;
```

## B3.225 VdevFromVdevId function

Returns the VDEV identified by vdev\_id and assigned to realm .

```
readonly func VdevFromVdevId( realm : RmmRealm, vdev_id : bits(64)) =>
```

```
RmmVdev
```

## B3.226 VdevGenerateNonce function

```
Generate a VDEV nonce.
```

```
VdevGenerateNonce(
```

```
readonly impdef func vdev : RmmVdev) => integer
```

## B3.227 VdevIdIsFree function

Returns TRUE if vdev\_id does not identify any device which is assigned to realm .

```
readonly func VdevIdIsFree( realm : RmmRealm, vdev_id : bits(64)) =>
```

## B3.228 VdevSid function

Returns physical SID for the specified VDEV.

```
readonly func VdevSid( vdev : RmmVdev) =>
```

## B3.229 VdevStateToRsi function

Get VDEV state

```
readonly func VdevStateToRsi( vdev_state : RmmVdevState) => RsiVdevState begin case vdev_state of when VDEV_NEW => return RSI_VDEV_UNLOCKED; when VDEV_UNLOCKED => return RSI_VDEV_UNLOCKED; when VDEV_LOCKED => return RSI_VDEV_LOCKED; when VDEV_STARTED => return RSI_VDEV_STARTED; when VDEV_ERROR => return RSI_VDEV_ERROR; when VDEV_KEY_REFRESH => return RSI_VDEV_STARTED; when VDEV_KEY_PURGE => return RSI_VDEV_STARTED; end; end;
```

## B3.230 VersionEqual function

Returns TRUE if command result matches the stated value.

```
pure func VersionEqual(
```

```
boolean bits(64)
```

B3.231. VmidsAvailable function

```
ver1 : PsciInterfaceVersion, ver2 : PsciInterfaceVersion) => boolean pure func VersionEqual( ver1 : RmiInterfaceVersion, ver2 : RmiInterfaceVersion) => boolean pure func VersionEqual( ver1 : RsiInterfaceVersion, ver2 : RsiInterfaceVersion) => boolean
```

## See also:

- [Chapter B2 Interface versioning](rmm-B2.md)

## B3.231 VmidsAvailable function

Returns TRUE if there are count unused VMIDs.

```
readonly func VmidsAvailable( count : integer) => boolean
```

## See also:

- [A5.6.2 RTT structure and configuration](rmm-A5.6.md#a562-rtt-structure-and-configuration)

## B3.232 VsidIsFree function

Returns TRUE if vsid is unused within the VSMMU vsmmu .

```
readonly func VsidIsFree( vsmmu : RmmVsmmu, vsid : bits(64)) =>
```

## B3.233 VsmmuAt function

```
boolean
```

Returns the VSMMU object located at physical address addr .

```
readonly func VsmmuAt( addr : Address) => RmmVsmmu
```

## See also:

- [A9.8 Virtual SMMU](rmm-A9.8.md)

## B3.234 VsmmuFeaturesAt function

Returns the RmiVsmmuFeatures object located at physical address addr .

```
readonly func VsmmuFeaturesAt(
```

```
addr : Address) => RmiVsmmuFeatures
```

## B3.235 VsmmuIsLive function

Returns TRUE if the VSMMU located at physical address addr is live.

```
readonly func VsmmuIsLive( addr : Address) =>
```

```
boolean
```

See also:

- [A9.8.3 VSMMU liveness](rmm-A9.8.md#a983-vsmmu-liveness)

