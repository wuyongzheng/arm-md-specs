## H5.5 CTI registers programmers' model

The CTI registers programmers' model is described in About the External Debug Registers. The following sections contain information specific to the CTI:

- External debug register resets.
- External debug interface register access permissions.
- Cross-trigger interface registers.
- The individual register descriptions in Cross-Trigger Interface registers.

See also Memory-mapped accesses to the external debug interface.

## H5.5.1 CTI reset

An External Debug reset resets the CTI. See External debug register resets for details of CTI register resets. All CTI output triggers and output channels are deasserted on an External Debug reset.

Note

An indirect read of an output trigger might not observe the deasserted state until the processor is Cold reset. For more information, see Synchronization of changes to the external debug registers.

## H5.5.2 CTI authentication

The CTI ignores the state of the IMPLEMENTATION DEFINED authentication interface. This means that:

- CTITRIGINSTATUS shows the status of the input triggers and CTICHINSTATUS shows the status of the input channels, regardless of the value of ExternalNoninvasiveDebugEnabled() .

Note

The PE does not generate the Cross-halt trigger event and the trace unit does not generate Generic trace external output trigger events when ExternalNoninvasiveDebugEnabled() == FALSE. However, the PE can generate Performance Monitors overflow trigger events.

- The CTI can generate external triggers regardless of the value of ExternalInvasiveDebugEnabled() .

Note

The PE ignores Debug request and Restart request trigger events when ExternalInvasiveDebugEnabled() is FALSE.

The trace unit ignores Generic trace external input trigger events when ExternalNoninvasiveDebugEnabled() is FALSE.

The behavior of Generic CTI interrupt requests is part of the IMPLEMENTATION DEFINED handling of these interrupts, but it is permissible for an interrupt controller to receive these requests even when ExternalInvasiveDebugEnabled() is FALSE.