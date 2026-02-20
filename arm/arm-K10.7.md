## K10.7 Use of the RAS Extension

## K10.7.1 Using DC {G}ZVA and DC CI{GD}VAPS to remove poison

- ITFLPJ

The following Software usage statements detail possible mechanisms used to remove poison from a Location. For more information, see Clearing Deferred errors from poisoned Locations.

SSLHGP

- SFCDTN

An error exception is generated when the PE consumes a poisoned Location. This might be a synchronous External Abort exception or an SError exception, depending on the implementation.

If software is able to recover from the exception, it will place the translation granule into quarantine by logging it as having a latent fault, and will not use it again.

If software needs to remove a translation granule from quarantine, it must remove the poison from the poisoned Location. This might be done directly by using architecture-defined mechanisms defined below, or accelerated by an IMPLEMENTATION DEFINED peripheral abstracted by a firmware call or other software interface.

Software can remove poison by using the following steps:

1. Discovering from firmware tables whether the DC ZVA or, if FEAT\_MTE2 is implemented, DC GZVA instruction is poison-atomic for the region of physical memory containing the poisoned Location.
2. If DC {G}ZVA is poison-atomic for the region, using one or more DC {G}ZVA instructions to remove the poison.

Otherwise, it is IMPLEMENTATION DEFINED whether an IMPLEMENTATION DEFINED mechanism exists to remove poison from a Location, including cached copies of the Location.

It might be acceptable to reuse the memory at this point, or wait some time for the Location to naturally be written back to memory, or be pushed to memory by an IMPLEMENTATION DEFINED mechanism.

The Location might remain in other caches, meaning that even if a DC {G}ZVA instruction has removed the poisoned copy, other copies might mask a persistent fault in main memory for the Location, until the Location is cleaned and invalidated from all caches and read again from main memory.

- STWYNP If FEAT\_PoPS is implemented, software can use a sequence of DC CI{GD}VAPS and IC IVAU instructions to ensure that all copies of a poisoned Location are removed after attempting to remove poison by using a poison-atomic DC {G}ZVA instruction or an IMPLEMENTATION DEFINED mechanism.
- IYTKLZ The DC {G}ZVA instructions write zeros to the Location. Any value can be written to the poison granule to remove poison if the write is poison-atomic.

Software might want to vary the value, for example to test the poison granule for stuck-at-one or stuck-at-zero faults.

However, Arm recommends that software uses DC {G}ZVA instructions first, if they are poison-atomic, and then overwrites the zeros with any other test pattern as necessary.

- SRDSYX After performing a clean and invalidate, software can verify that poison has been removed with a Read of the Location. The clean and invalidate of the Location is required to be Ordered-before the Memory Read Effect.

If the Read does not read back the value written to the Location, this might be due to one of the following:

- The Location remains poisoned.
- The error is persistent.
- If FEAT\_MEC is implemented, different keys were used for the write and subsequent read.
- The Location was accessed with mismatched attributes.

If the error condition persists after attempting to clear the fault again, then the translation granule should be returned to quarantine.

Software may choose to implement different levels of quarantine, to avoid repeatedly attempting to remove poison from a Location with a known persistent error. That is, treat the translation granule as permanently corrupted and off-line until the next system reboot. Software might want to analyze these Locations further to diagnose the fault.