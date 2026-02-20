## I5.6 Generic Timer memory-mapped registers overview

The Generic Timer memory-mapped registers are implemented as multiple register frames, with each register frame having its own base address, as follows:

- Asingle CNTCTLBase register frame, at base address CNTCTLBase.
- Between one and seven CNTBase N register frames, each with its own base address CNTBase N .
- For each CNTBase N register frame, if required, a CNTEL0Base N register frame, at base address CNTEL0Base N , that provides an EL0 view of the CNTBase N register frame.

For more information, see:

- Memory-mapped timer components.
- The CNTBaseN and CNTEL0BaseN frames. This section includes the memory map of the CNTBase N and CNTBase N register frames.
- The CNTCTLBase frame. This section includes the memory map of the CNTCTLBase register frame.

Note

Providing a complete set of features in a system level implementation gives an implementation example for a system level implementation of the Generic Timer.