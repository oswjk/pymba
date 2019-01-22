
class VimbaException(Exception):
    ERROR_CODES = (
        # 0
        ERR_NO_ERROR,

        # -1 to -19
        ERR_UNEXPECTED_FAULT,
        ERR_STARTUP_NOT_CALLED,
        ERR_INSTANCE_NOT_FOUND,
        ERR_HANDLE_INVALID,
        ERR_DEVICE_NOT_OPENED,
        ERR_OPERATION_INVALID_FOR_ACCESS_MODE,
        ERR_PARAMETER_INVALID,
        ERR_STRUCT_SIZE_INVALID,
        ERR_DATA_TOO_LARGE,
        ERR_FEATURE_TYPE_WRONG,
        ERR_VALUE_INVALID,
        ERR_TIMEOUT,
        ERR_OTHER_ERROR,
        ERR_RESOURCE_NOT_AVAILABLE,
        ERR_CALL_INVALID,
        ERR_TRANSPORT_LAYER_NOT_FOUND,
        ERR_FEATURE_NOT_IMPLEMENTED,
        ERR_FEATURE_NOT_SUPPORTED,
        ERR_PARTIAL_REGISTER_ACCESS,

        # -50 to -56
        ERR_CAMERA_NOT_FOUND,
        ERR_FRAME_BUFFER_MEMORY,
        ERR_INVALID_INPUT,
        ERR_FEATURE_NOT_FOUND,
        ERR_INTERFACE_NOT_FOUND,
        ERR_NOT_IMPLEMENTED_IN_PYMBA,
        ERR_UNDEFINED_ERROR_CODE,
    ) = tuple(range(0, -20, -1)) + tuple(range(-50, -57, -1))

    ERRORS = {
        # Vimba C API specific errors
        ERR_NO_ERROR: 'No error.',
        ERR_UNEXPECTED_FAULT: 'Unexpected fault in VimbaC or driver.',
        ERR_STARTUP_NOT_CALLED: 'VmbStartup() was not called before the current command.',
        ERR_INSTANCE_NOT_FOUND: 'The designated instance (camera, feature etc.) cannot be found.',
        ERR_HANDLE_INVALID: 'The given handle is not valid, ensure device open.',
        ERR_DEVICE_NOT_OPENED: 'Device was not opened for usage.',
        ERR_OPERATION_INVALID_FOR_ACCESS_MODE: 'Operation is invalid with the current access mode.',
        ERR_PARAMETER_INVALID: 'One of the parameters was invalid (usually an illegal pointer).',
        ERR_STRUCT_SIZE_INVALID: 'The given struct size is not valid for this version of the API.',
        ERR_DATA_TOO_LARGE: 'More data was returned in a string/list than space was provided.',
        ERR_FEATURE_TYPE_WRONG: 'The feature type for this access function was wrong.',
        ERR_VALUE_INVALID: 'The value was not valid; either out of bounds or not an increment of the minimum.',
        ERR_TIMEOUT: 'Timeout during wait.',
        ERR_OTHER_ERROR: 'Other error.',
        ERR_RESOURCE_NOT_AVAILABLE: 'Resources not available (e.g. memory).',
        ERR_CALL_INVALID: 'Call is invalid in the current context (e.g. callback).',
        ERR_TRANSPORT_LAYER_NOT_FOUND: 'No transport layers were found.',
        ERR_FEATURE_NOT_IMPLEMENTED: 'API feature is not implemented.',
        ERR_FEATURE_NOT_SUPPORTED: 'API feature is not supported.',
        ERR_PARTIAL_REGISTER_ACCESS: 'A multiple registers read or write was partially completed.',

        # Custom errors
        ERR_CAMERA_NOT_FOUND: 'Could not find the specified camera.',
        ERR_FRAME_BUFFER_MEMORY: 'Not enough memory to assign frame buffer.',
        ERR_INVALID_INPUT: 'Invalid input.',
        ERR_FEATURE_NOT_FOUND: 'Could not find the specified feature.',
        ERR_INTERFACE_NOT_FOUND: 'Could not find the specified interface.',
        ERR_NOT_IMPLEMENTED_IN_PYMBA: 'This function is not yet implemented in Pymba',
        ERR_UNDEFINED_ERROR_CODE: 'Undefined error code',
    }

    @property
    def message(self):
        return self.ERRORS[self.error_code]

    def __init__(self, error_code: int):
        if error_code not in self.ERROR_CODES:
            error_code = self.ERR_UNDEFINED_ERROR_CODE
        self.error_code = error_code

        super().__init__(self.message)
