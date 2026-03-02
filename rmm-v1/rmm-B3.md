## Chapter B3

## Command condition functions

This chapter describes functions which are used in command condition expressions.

See also:

- B1.4 Command condition expressions

## B3.1 AddrInRange function

Returns TRUE if addr is within [base, base+size] .

```
func AddrInRange( addr : Address, base : Address, size : integer) => boolean begin return ((UInt(addr) >= UInt(base)) && (UInt(addr) <= UInt(base) + end
```

```
size));
```

## B3.2 AddrIsAligned function

Returns TRUE if address addr is aligned to an n byte boundary.

```
func AddrIsAligned( addr : Address, n : integer) =>
```

```
boolean
```

## B3.3 AddrIsGranuleAligned function

Returns TRUE if address addr is aligned to the size of a Granule.

```
func AddrIsGranuleAligned( addr : Address) => boolean func AddrIsGranuleAligned( addr : integer) => boolean
```

## See also:

- A2.2 Granule

## B3.4 AddrIsProtected function

Returns TRUE if address addr is a Protected IPA for realm .

```
func AddrIsProtected( addr : Address, realm : RmmRealm) => boolean begin return UInt(addr) < 2^(realm.ipa_width -end
```

## B3.5 AddrIsRttLevelAligned function

Returns TRUE if Address addr is aligned to the size of the address range described by an RTTE in a level level RTT.

Returns FALSE if level is invalid.

```
func AddrIsRttLevelAligned( addr : Address, level : integer) =>
```

```
boolean
```

## B3.6 AddrRangeIsProtected function

Returns TRUE if all addresses in range [base, top) are Protected IPAs for realm .

```
func AddrRangeIsProtected( base : Address, top : Address, realm : RmmRealm) => boolean begin var size = UInt(top) -UInt(base); return (AddrIsProtected(base, realm) && size > 0 && size < 2^realm.ipa_width && AddrIsProtected(ToAddress(UInt(top) -1), realm)); end
```

## B3.7 AlignDownToRttLevel function

Round down addr to align to the size of the address range described by an RTTE in a level level RTT.

```
func AlignDownToRttLevel( addr : Address, level : integer) => Address
```

```
1);
```

## B3.8 AlignUpToRttLevel function

Round up addr to align to the size of the address range described by an RTTE in a level level RTT.

```
func AlignUpToRttLevel( addr : Address, level : integer) =>
```

## B3.9 AuxAlias function

Returns TRUE if any of the first count entries in a list of auxiliary Granule addresses are aliased - either among themselves, or with the REC address itself.

```
func AuxAlias( rec : Address, aux : array [16] of Address, count : integer) => boolean begin assert 0 <= count && count <= 16; var sorted = AuxSort(aux, count); for i = 0 to count -1 do if sorted[i] == rec then return TRUE; end if i >= 1 && sorted[i] == sorted[i -1] return TRUE; end end return FALSE; end
```

## B3.10 AuxAligned function

Returns TRUE if the first count entries in a list of auxiliary Granule addresses are aligned to the size of a Granule.

```
func AuxAligned( aux : array [16] of Address, count : integer) => boolean begin assert 0 <= count && count <= 16; for i = 0 to count -1 do if !AddrIsGranuleAligned(aux[i]) return FALSE; end end return TRUE; end
```

## B3.11 AuxEqual function

Returns TRUE if the first count entries in two lists of auxiliary Granule addresses are equal.

```
func AuxEqual( aux1 : array [16] of Address, aux2 : array [16] of Address, count : integer) => boolean begin
```

```
then
```

```
then
```

```
Address
```

Chapter B3. Command condition functions B3.12. AuxSort function

```
assert 0 <= count && count <= 16; for i = 0 to count -1 do if aux1[i] != aux2[i] then return FALSE; end end return TRUE; end
```

## B3.12 AuxSort function

Sort first count entries in array of auxiliary Granule addresses.

```
func AuxSort( addrs : array [16] of Address, count : integer) => array [16] of
```

## B3.13 AuxStateEqual function

Returns TRUE if the state of the first count entries in a list of auxiliary Granule addresses is equal to state .

```
func AuxStateEqual( aux : array [16] of Address, count : integer, state : RmmGranuleState) => boolean begin assert 0 <= count && count <= 16; for i = 0 to count -1 do if (!PaIsDelegable(aux[i]) || Granule(aux[i]).state != state) then return FALSE; end end return TRUE; end
```

## B3.14 AuxStates function

Inductive function which identifies the states of the first count entries in a list of auxiliary Granules.

This function is used in the definition of command footprint.

```
func AuxStates( aux : array [16] of count : integer)
```

```
Address,
```

## B3.15 CurrentRealm function

```
Returns the current Realm. func CurrentRealm() => RmmRealm
```

## B3.16 CurrentRec function

Returns the current REC.

```
func CurrentRec() => RmmRec
```

```
Address
```

## B3.17 Equal function

Check whether concrete and abstract values are equal

| func Equal( abstract                                                                      | : :                                                                                                                                                                                                                               |          |                   |            |            |
|-------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------------------|------------|------------|
| concrete func Equal(                                                                      | RmmFeature, RmiFeature) => boolean                                                                                                                                                                                                |          |                   |            |            |
| concrete abstract func Equal( abstract concrete                                           | RmiFeature, RmmFeature) =>                                                                                                                                                                                                        |          | : : : :           |            |            |
| func Equal( concrete abstract func Equal( abstract concrete func Equal( concrete          | boolean RmiHashAlgorithm, RmmHashAlgorithm) => boolean RmmRecRunnable,                                                                                                                                                            |          | : : :             |            |            |
| func Equal( abstract concrete func Equal( concrete abstract func Equal( abstract concrete | RmmHashAlgorithm, RmiHashAlgorithm) => boolean RmiRecRunnable) => boolean RmiRecRunnable, RmmRecRunnable) => boolean RmmRipas, RmiRipas) => boolean RmiRipas, RmmRipas) => boolean RmmHashAlgorithm, RsiHashAlgorithm) => boolean | abstract | : : : : : : : : : |            |            |
| func                                                                                      | : RsiHashAlgorithm, RmmHashAlgorithm) => boolean                                                                                                                                                                                  |          |                   |            |            |
| Equal( concrete                                                                           | :                                                                                                                                                                                                                                 |          |                   |            |            |
| func Equal( func Equal(                                                                   | : RsiRipas) => boolean                                                                                                                                                                                                            |          |                   |            |            |
|                                                                                           | RsiRipas, RmmRipas) => boolean                                                                                                                                                                                                    |          |                   |            |            |
| func Equal(                                                                               |                                                                                                                                                                                                                                   |          |                   |            |            |
|                                                                                           | RmmRipasChangeDestroyed, RsiRipasChangeDestroyed) =>                                                                                                                                                                              |          |                   |            |            |
|                                                                                           | boolean                                                                                                                                                                                                                           |          |                   |            |            |
| func Equal( concrete                                                                      |                                                                                                                                                                                                                                   |          |                   |            |            |
| concrete                                                                                  |                                                                                                                                                                                                                                   |          |                   |            |            |
| abstract concrete                                                                         | : RmmRipas,                                                                                                                                                                                                                       |          |                   |            |            |
| abstract                                                                                  |                                                                                                                                                                                                                                   |          |                   |            |            |
|                                                                                           | :                                                                                                                                                                                                                                 |          |                   |            |            |
| abstract                                                                                  | RsiRipasChangeDestroyed, :                                                                                                                                                                                                        |          |                   |            |            |
|                                                                                           | RmmRipasChangeDestroyed) boolean                                                                                                                                                                                                  |          |                   |            |            |
|                                                                                           | =>                                                                                                                                                                                                                                |          |                   |            |            |
|                                                                                           | :                                                                                                                                                                                                                                 | abstract |                   |            |            |
|                                                                                           |                                                                                                                                                                                                                                   |          | :                 | abstract : | concrete : |

See also:

B3.18. Gicv3ConfigIsValid function

- B1.8 Concrete and abstract types

## B3.18 Gicv3ConfigIsValid function

Returns TRUE if the values of all gicv3\_* attributes are valid.

```
func Gicv3ConfigIsValid( gicv3_hcr : bits(64), gicv3_lrs : array [16] of bits(64)) =>
```

## See also:

- A6.1 Realm interrupts
- B4.4.14 RmiRecEnter type

## B3.19 Granule function

Returns the Granule located at physical address addr .

```
func Granule( addr : Address) =>
```

## See also:

- A2.2 Granule

## B3.20 GranuleAccessPermitted function

Returns TRUE if the Granule located at physical address addr is accessible via pas .

```
func GranuleAccessPermitted( addr : Address, pas : RmmPhysicalAddressSpace) => boolean begin case Granule(addr).gpt of when GPT_NS => return (pas == PAS_NS); when GPT_REALM => return (pas == PAS_REALM); when GPT_SECURE => return (pas == PAS_SECURE); when GPT_ROOT => return (pas == PAS_ROOT); when GPT_AAP => return TRUE; end end
```

## B3.21 ImplFeatures function

Returns features supported by the implementation.

```
func ImplFeatures() =>
```

```
RmmFeatures
```

## B3.22 MinAddress function

Returns the smaller of two addresses.

```
func MinAddress( addr1 : Address, addr2 : Address) => Address begin return ToAddress(Min(UInt(addr1), UInt(addr2)));
```

```
RmmGranule
```

```
boolean
```

end

## B3.23 MpidrEqual function

Returns TRUE if the specified MPIDR values are logically equivalent.

```
func MpidrEqual( rmm_mpidr : bits(64), rmi_mpidr : RmiRecMpidr) => boolean begin return (rmm_mpidr[ 3: 0] == rmi_mpidr.aff0 && rmm_mpidr[15: 8] == rmi_mpidr.aff1 && rmm_mpidr[23:16] == rmi_mpidr.aff2 && rmm_mpidr[31:24] == rmi_mpidr.aff3); end
```

## B3.24 MpidrIsUsed function

Returns TRUE if the specified MPIDR value identifies a REC in the current Realm.

```
func MpidrIsUsed( mpidr : bits(64)) =>
```

```
boolean
```

## B3.25 PaIsDelegable function

Returns TRUE if the Granule located at physical address addr is delegable.

```
func PaIsDelegable( addr : Address) =>
```

```
boolean
```

## B3.26 PsciReturnCodeEncode function

Return encoding for a PsciReturnCode value.

```
func PsciReturnCodeEncode( value : PsciReturnCode) =>
```

```
bits(64)
```

## B3.27 PsciReturnCodePermitted function

Whether a PSCI return code is permitted.

```
func PsciReturnCodePermitted( calling_rec : RmmRec, target_rec : RmmRec, value : PsciReturnCode) => boolean begin if value == PSCI_SUCCESS then return TRUE; end var fid : bits(64) = calling_rec.gprs[0]; // Host is permitted to deny a PSCI_CPU_ON request, if the // CPU is not already on. if (fid == FID_PSCI_CPU_ON && target_rec.flags.runnable != RUNNABLE && value == PSCI_DENIED) then return TRUE;
```

```
target
```

Chapter B3. Command condition functions B3.28. ReadMemory function

```
end return FALSE; end
```

## See also:

- A4.3.7 REC exit due to PSCI
- B4.3.7 RMI\_PSCI\_COMPLETE command

## B3.28 ReadMemory function

Read contents of memory at address range [addr + offset, addr + offset + size)

offset and size are both numbers of bytes.

```
func ReadMemory( addr : bits(64), offset : integer, size : integer) => bits(size *
```

## B3.29 Realm function

Returns the Realm whose RD is located at physical address addr .

```
func Realm( addr : Address) =>
```

## See also:

- A2.1 Realm

## B3.30 RealmConfig function

Returns Realm configuration stored at IPA addr , mapped in the current Realm.

```
func RealmConfig( addr : Address) =>
```

```
RsiRealmConfig
```

## B3.31 RealmHostCall function

Returns Host call data stored at IPA addr , mapped in the current Realm.

```
func RealmHostCall( addr : Address) =>
```

```
RsiHostCall
```

## B3.32 RealmIsLive function

Returns TRUE if the Realm whose RD is located at physical address addr is live.

```
func RealmIsLive( addr : Address) =>
```

## See also:

- A2.1.4 Realm liveness

```
boolean
```

```
RmmRealm
```

```
8)
```

## B3.33 RealmParams function

Returns Realm parameters stored at physical address addr .

If the PAS of addr is not NS, the return value is UNKNOWN.

```
func RealmParams( addr : Address) => RmiRealmParams
```

## See also:

- A2.1.6 Realm parameters

## B3.34 RealmParamsSupported function

Returns TRUE if the Realm parameters are supported by the implementation.

```
func RealmParamsSupported( value : RmiRealmParams) =>
```

```
boolean
```

## B3.35 Rec function

Returns the REC object located at physical address addr .

```
func Rec( addr : Address) =>
```

```
RmmRec
```

## See also:

- A2.3 Realm Execution Context

## B3.36 RecAuxCount function

Returns the number of auxiliary Granules required for a REC in the Realm described by rd .

The return value is guaranteed not to be greater than 16.

For a given Realm, this function always returns the same value.

```
func RecAuxCount( rd : Address) =>
```

```
integer
```

## B3.37 RecFromMpidr function

Returns the REC object identified by the specified MPIDR value, in the current Realm.

```
func RecFromMpidr( mpidr : bits(64)) =>
```

```
RmmRec
```

## B3.38 RecIndex function

Returns the REC index which corresponds to mpidr .

```
func RecIndex( mpidr : RmiRecMpidr) => integer begin return (UInt(mpidr.aff0) + 16 * UInt(mpidr.aff1) + 16 * 256 * UInt(mpidr.aff2)
```

B3.39. RecParams function

```
+ 16 * 256 * 256 * UInt(mpidr.aff3)); end
```

See also:

- A2.3.3 REC index and MPIDR value

## B3.39 RecParams function

Returns REC parameters stored at physical address addr .

If the PAS of addr is not NS, the return value is UNKNOWN.

```
func RecParams( addr : Address) =>
```

```
RmiRecParams
```

## B3.40 RecRipasChangeResponse function

Returns response to RIPAS change request.

```
then
```

```
func RecRipasChangeResponse( rec : RmmRec) => RsiResponse begin if ((rec.ripas_value == RAM) && (rec.ripas_addr != rec.ripas_top) && (rec.ripas_response == REJECT)) return RSI_REJECT; end return RSI_ACCEPT; end
```

## See also:

- A5.4 RIPAS change

## B3.41 RecRun function

Returns the RecRun object stored at physical address addr .

```
func RecRun( addr : Address) => RmiRecRun
```

## See also:

- A4.2 REC entry
- A4.3 REC exit

## B3.42 RemExtend function

Extend REM, using size LSBs from new\_value , with the remaining bits zero-padded to form a 512-bit value.

```
func RemExtend( hash_algo : RmmHashAlgorithm, old_value : RmmRealmMeasurement, new_value : RmmRealmMeasurement, size : integer) =>
```

See also:

```
RmmRealmMeasurement
```

- A7.1.2 Realm Extensible Measurement

## B3.43 ResultEqual function

Returns TRUE if command result matches the stated value.

```
func ResultEqual( result : RmiCommandReturnCode, status : RmiStatusCode) =>
```

```
func ResultEqual( result : status : RmiStatusCode, index : integer) => boolean
```

```
boolean RmiCommandReturnCode,
```

## B3.44 RimExtendData function

Extend RIM with contribution from DATA creation.

```
func RimExtendData( realm : RmmRealm, ipa : Address, data : Address, flags : RmiDataFlags) =>
```

See also:

- B4.3.1.4 RMI\_DATA\_CREATE extension of RIM

## B3.45 RimExtendRec function

Extend RIM with contribution from REC creation.

```
func RimExtendRec( realm : RmmRealm, params : RmiRecParams) => RmmRealmMeasurement
```

See also:

- B4.3.12.4 RMI\_REC\_CREATE extension of RIM

## B3.46 RimExtendRipas function

Extend RIM with contribution from RIPAS change for an IPA range.

```
func RimExtendRipas( realm : RmmRealm, base : Address, top : Address, level : integer) => RmmRealmMeasurement begin var rim = realm.measurements[0]; var size = RttLevelSize(level); var addr = base; while (UInt(addr) < UInt(top)) do rim = RimExtendRipasForEntry(rim, addr, level); addr = ToAddress(UInt(addr) + size); end
```

```
RmmRealmMeasurement
```

Chapter B3. Command condition functions B3.47. RimExtendRipasForEntry function

```
return rim; end
```

## See also:

- B4.3.18.4 RMI\_RTT\_INIT\_RIPAS extension of RIM

## B3.47 RimExtendRipasForEntry function

Extend RIM with contribution from RIPAS change for a single RTT entry.

```
func RimExtendRipasForEntry( rim : RmmRealmMeasurement, ipa : Address, level : integer) =>
```

```
RmmRealmMeasurement
```

## B3.48 RimInit function

## Initialize RIM.

```
func RimInit( hash_algo : RmmHashAlgorithm, params : RmiRealmParams) =>
```

## See also:

- B4.3.9.4 RMI\_REALM\_CREATE initialization of RIM

## B3.49 RipasToRmi function

## Encodes a RIPAS value.

```
func RipasToRmi( ripas : RmmRipas) => RmiRipas begin case ripas of when EMPTY => return RMI_EMPTY; when RAM => return RMI_RAM; when DESTROYED => return RMI_DESTROYED; end end
```

## B3.50 RmiRealmParamsIsValid function

Returns TRUE if the memory location contains a valid encoding of the RmiRealmParams type.

```
func RmiRealmParamsIsValid( addr : Address) =>
```

```
boolean
```

## B3.51 Rtt function

Returns the RTT at address rtt .

```
func Rtt( addr : Address) =>
```

```
RmmRtt
```

```
RmmRealmMeasurement
```

## B3.52 RttAllEntriesContiguous function

Returns TRUE if all entries in the RTT at address rtt at level level have contiguous output addresses, starting with addr .

```
func RttAllEntriesContiguous( rtt : RmmRtt, addr : Address, level : integer) =>
```

See also:

- A5.5 Realm Translation Table

## B3.53 RttAllEntriesRipas function

Returns TRUE if all entries in the RTT at address rtt have RIPAS ripas .

```
func RttAllEntriesRipas( rtt : RmmRtt, ripas : RmmRipas) =>
```

```
boolean
```

## B3.54 RttAllEntriesState function

Returns TRUE if all entries in the RTT at address rtt have state state .

```
func RttAllEntriesState( rtt : RmmRtt, state : RmmRttEntryState) =>
```

See also:

- A5.5 Realm Translation Table

## B3.55 RttConfigIsValid function

Returns TRUE if the RTT configuration values provided are self-consistent and are supported by the platform.

```
func RttConfigIsValid( ipa_width : integer, rtt_level_start : integer, rtt_num_start : integer) =>
```

See also:

- A5.5 Realm Translation Table

## B3.56 RttDescriptorIsValidForUnprotected function

Returns TRUE if, within the descriptor desc , all of the following are true:

- All fields which are Host-controlled RTT attributes are set to architecturally valid values.
- All fields which are not Host-controlled RTT attributes are set to zero.

```
func RttDescriptorIsValidForUnprotected( desc : bits(64)) => boolean
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

- A5.5.11 RTT entry attributes

## B3.57 RttEntriesInRangeRipas function

Returns TRUE if all entries in the RTT at address rtt at level level , within IPA range [base, top), have RIPAS

```
ripas .
```

```
func RttEntriesInRangeRipas( rtt : RmmRtt, level : integer, base : Address, top : Address, ripas : RmmRipas) =>
```

```
boolean
```

## B3.58 RttEntry function

Returns the i th entry in the RTT at address rtt .

```
func RttEntry( rtt : Address, i : integer) => RmmRttEntry
```

See also:

- A5.5 Realm Translation Table

## B3.59 RttEntryFromDescriptor function

Converts a descriptor to an RmmRttEntry object.

```
func RttEntryFromDescriptor( desc : bits(64)) =>
```

```
RmmRttEntry
```

## B3.60 RttEntryIndex function

Returns the index of the entry in a level level RTT which is identified by addr .

```
func RttEntryIndex( addr : Address, level : integer) =>
```

```
integer
```

See also:

- A5.5 Realm Translation Table

## B3.61 RttEntryState function

Encodes the state of an RTTE.

```
func RttEntryState( state : RmmRttEntryState) => RmiRttEntryState begin case state of when UNASSIGNED => return RMI_UNASSIGNED; when ASSIGNED => return RMI_ASSIGNED; when UNASSIGNED_NS => return RMI_UNASSIGNED; when ASSIGNED_NS => return RMI_ASSIGNED; when TABLE => return RMI_TABLE;
```

Chapter B3. Command condition functions B3.62. RttFold function

```
end end
```

## B3.62 RttFold function

Returns the RTTE which results from folding the homogeneous RTT at address rtt .

```
func RttFold( rtt : RmmRtt) =>
```

See also:

- A5.5.6 RTT folding

## B3.63 RttIsHomogeneous function

Returns TRUE if the RTT at address rtt is homogeneous.

```
func RttIsHomogeneous( rtt : RmmRtt) =>
```

```
boolean
```

See also:

- A5.5.6 RTT folding

## B3.64 RttIsLive function

Returns TRUE if the RTT at address rtt is live.

```
func RttIsLive( rtt : RmmRtt) =>
```

```
boolean
```

## See also:

- A5.5.8 RTTE liveness and RTT liveness
- A5.5.9 RTT destruction

## B3.65 RttLevelIsBlockOrPage function

Returns TRUE if level is either a block or page RTT level for the Realm described by rd .

```
func RttLevelIsBlockOrPage( rd : Address, level : integer) =>
```

See also:

- A5.5 Realm Translation Table

## B3.66 RttLevelIsStarting function

Returns TRUE if level is the starting level of the RTT for the Realm described by rd .

```
func RttLevelIsStarting( rd : Address, level : integer) =>
```

See also:

```
boolean
```

```
boolean
```

```
RmmRttEntry
```

- A5.5 Realm Translation Table

## B3.67 RttLevelIsValid function

Returns TRUE if level is a valid RTT level for the Realm described by rd .

```
func RttLevelIsValid( rd : Address, level : integer) =>
```

```
boolean
```

## See also:

- A5.5 Realm Translation Table

## B3.68 RttLevelSize function

Returns the size of the address space described by each entry in an RTT at level.

If level is invalid, the return value is UNKNOWN.

```
func RttLevelSize( level : integer) =>
```

```
integer
```

## See also:

- A5.5 Realm Translation Table

## B3.69 RttsAllProtectedEntriesRipas function

Returns TRUE if the RIPAS of all entries identified by Protected IPAs in all of the starting-level RTT Granules is equal to ripas .

```
func RttsAllProtectedEntriesRipas( rtt_base : Address, rtt_num_start : integer, ripas : RmmRipas) => boolean
```

## B3.70 RttsAllProtectedEntriesState function

Returns TRUE if the state of all entries identified by Protected IPAs in all of the starting-level RTT Granules is equal to state .

```
func RttsAllProtectedEntriesState( rtt_base : Address, rtt_num_start : integer, state : RmmRttEntryState) =>
```

```
boolean
```

## B3.71 RttsAllUnprotectedEntriesState function

Returns TRUE if the state of all entries identified by Unprotected IPAs in all of the starting-level RTT Granules is equal to state .

```
func RttsAllUnprotectedEntriesState( rtt_base : Address, rtt_num_start : integer, state : RmmRttEntryState) =>
```

```
boolean
```

## B3.72 RttsGranuleState function

Inductive function which identifies the states of the starting-level RTT Granules.

This function is used in the definition of command footprint.

```
func RttsGranuleState( rtt_base : Address, rtt_num_start :
```

```
integer)
```

## B3.73 RttSkipEntriesUnlessRipas function

Scanning rtt starting from ipa , returns the IPA of the first entry whose RIPAS is ripas .

If no entry is found whose RIPAS is ripas , returns the next IPA after the last entry in rtt .

The return value is aligned to the size of the address range described by an entry at RTT level .

```
func RttSkipEntriesUnlessRipas( rtt : RmmRtt, level : integer, ipa : Address, ripas : RmmRipas) => Address
```

## B3.74 RttSkipEntriesUnlessState function

Scanning rtt starting from ipa , returns the IPA of the first entry whose state is state .

If no entry is found whose state is state , returns the next IPA after the last entry in rtt .

The return value is aligned to the size of the address range described by an entry at RTT level .

```
func RttSkipEntriesUnlessState( rtt : RmmRtt, level : integer, ipa : Address, state : RmmRttEntryState) =>
```

```
Address
```

## B3.75 RttSkipEntriesWithRipas function

Scan rtt starting from base and terminating at top .

- If stop\_at\_destroyed is FALSE then return IPA of the first entry whose state is TABLE.
- If stop\_at\_destroyed is TRUE then return IPA of the first entry whose state is TABLE or whose RIPAS is DESTROYED.

If no such entry is found, returns the smaller of:

- The next IPA after the last entry in rtt
- The top argument.

The return value is aligned to the size of the address range described by an entry at RTT level .

```
func RttSkipEntriesWithRipas( rtt : RmmRtt, level : integer, base : Address, top : Address, stop_at_destroyed : boolean) => Address begin var result : Address = RttSkipEntriesUnlessState( rtt, level, base, TABLE);
```

```
if stop_at_destroyed then result = MinAddress(result, RttSkipEntriesUnlessRipas( rtt, level, base, DESTROYED)); end result = MinAddress(result, top); return AlignDownToRttLevel(result, level); end
```

## B3.76 RttSkipNonLiveEntries function

Scanning rtt starting from ipa , returns the IPA of the first live entry.

If no live entry is found, returns the next IPA after the last entry in rtt .

The return value is aligned to the size of the address range described by an entry at RTT level .

```
func RttSkipNonLiveEntries( rtt : RmmRtt, level : integer, ipa : Address) => Address begin var result : Address = RttSkipEntriesUnlessState( rtt, level, ipa, ASSIGNED); result = MinAddress(result, RttSkipEntriesUnlessState( rtt, level, ipa, ASSIGNED_NS)); result = MinAddress(result, RttSkipEntriesUnlessState( rtt, level, ipa, TABLE)); return AlignDownToRttLevel(result, level); end
```

## See also:

- A5.5.8 RTTE liveness and RTT liveness

## B3.77 RttsStateEqual function

Returns TRUE if the state of all of the starting-level RTT Granules is equal to state .

```
func RttsStateEqual( rtt_base : Address, rtt_num_start : integer, state : RmmGranuleState) => boolean begin for i = 0 to rtt_num_start -1 do var addr = (UInt(rtt_base) + i * RMM_GRANULE_SIZE)[(ADDRESS_WIDTH-1):0]; if (!PaIsDelegable(addr) || Granule(addr).state != state) then return FALSE; end end
```

B3.78. RttWalk function

```
return TRUE; end
```

## B3.78 RttWalk function

Returns the result of an RTT walk from the RTT base of rd to address addr .

If level is provided, the walk terminates at level .

```
func RttWalk( rd : Address, addr : Address) => RmmRttWalkResult func RttWalk( rd : Address, addr : Address, level : integer) => RmmRttWalkResult
```

See also:

- A5.5.10 RTT walk

## B3.79 ToAddress function

```
Convert integer to Address.
```

```
Address
```

```
bits(64)
```

```
func ToAddress(value : integer) => begin return value[(ADDRESS_WIDTH-1):0]; end
```

## B3.80 ToBits64 function

```
Convert integer to Bits64.
```

```
func ToBits64(value : integer) => begin return value[63:0]; end
```

## B3.81 VmidIsFree function

```
Returns TRUE if vmid is unused.
```

```
func VmidIsFree( vmid : bits(16)) =>
```

```
boolean
```

## B3.82 VmidIsValid function

Returns TRUE if vmid is valid on the platform.

```
func VmidIsValid( vmid : bits(16)) =>
```

```
boolean
```

If the underlying hardware platform does not implement FEAT\_VMID16 then a VMID value with vmid[15:8] != 0 is invalid.

See also:

Chapter B3. Command condition functions B3.82. VmidIsValid function

- A2.1.3 Realm attributes
- B4.3.9 RMI\_REALM\_CREATE command