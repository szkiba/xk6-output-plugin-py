# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from xk6_output_plugin_py import output_pb2 as xk6__output__plugin__py_dot_output__pb2


class OutputStub(object):
    """Output is the gRPC service to be implemented by output plugins.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Init = channel.unary_unary(
                '/xk6_output_plugin.output.Output/Init',
                request_serializer=xk6__output__plugin__py_dot_output__pb2.InitRequest.SerializeToString,
                response_deserializer=xk6__output__plugin__py_dot_output__pb2.InitResponse.FromString,
                )
        self.Start = channel.unary_unary(
                '/xk6_output_plugin.output.Output/Start',
                request_serializer=xk6__output__plugin__py_dot_output__pb2.Empty.SerializeToString,
                response_deserializer=xk6__output__plugin__py_dot_output__pb2.Empty.FromString,
                )
        self.Stop = channel.unary_unary(
                '/xk6_output_plugin.output.Output/Stop',
                request_serializer=xk6__output__plugin__py_dot_output__pb2.Empty.SerializeToString,
                response_deserializer=xk6__output__plugin__py_dot_output__pb2.Empty.FromString,
                )
        self.AddMetrics = channel.unary_unary(
                '/xk6_output_plugin.output.Output/AddMetrics',
                request_serializer=xk6__output__plugin__py_dot_output__pb2.AddMetricsRequest.SerializeToString,
                response_deserializer=xk6__output__plugin__py_dot_output__pb2.Empty.FromString,
                )
        self.AddSamples = channel.unary_unary(
                '/xk6_output_plugin.output.Output/AddSamples',
                request_serializer=xk6__output__plugin__py_dot_output__pb2.AddSamplesRequest.SerializeToString,
                response_deserializer=xk6__output__plugin__py_dot_output__pb2.Empty.FromString,
                )


class OutputServicer(object):
    """Output is the gRPC service to be implemented by output plugins.
    """

    def Init(self, request, context):
        """Init is called before registering the output plugin.

        Init receives the environment variables of the k6 process as parameters.
        In addition, standard command line arguments can be used to configure the plugin.
        A description of the plugin and various configuration parameters for the xk6-output-plugin can be returned.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Start(self, request, context):
        """Start is called before the k6 Engine tries to use the output and should be
        used for any long initialization tasks.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Stop(self, request, context):
        """Flush all remaining metrics and finalize the test run.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddMetrics(self, request, context):
        """AddMetrics is called on all metrics, the plugin can use it to save metric parameters.

        The call is made before AddSample is called with the given metric's sample.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddSamples(self, request, context):
        """AddSamples receives samples of the metrics periodically.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OutputServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Init': grpc.unary_unary_rpc_method_handler(
                    servicer.Init,
                    request_deserializer=xk6__output__plugin__py_dot_output__pb2.InitRequest.FromString,
                    response_serializer=xk6__output__plugin__py_dot_output__pb2.InitResponse.SerializeToString,
            ),
            'Start': grpc.unary_unary_rpc_method_handler(
                    servicer.Start,
                    request_deserializer=xk6__output__plugin__py_dot_output__pb2.Empty.FromString,
                    response_serializer=xk6__output__plugin__py_dot_output__pb2.Empty.SerializeToString,
            ),
            'Stop': grpc.unary_unary_rpc_method_handler(
                    servicer.Stop,
                    request_deserializer=xk6__output__plugin__py_dot_output__pb2.Empty.FromString,
                    response_serializer=xk6__output__plugin__py_dot_output__pb2.Empty.SerializeToString,
            ),
            'AddMetrics': grpc.unary_unary_rpc_method_handler(
                    servicer.AddMetrics,
                    request_deserializer=xk6__output__plugin__py_dot_output__pb2.AddMetricsRequest.FromString,
                    response_serializer=xk6__output__plugin__py_dot_output__pb2.Empty.SerializeToString,
            ),
            'AddSamples': grpc.unary_unary_rpc_method_handler(
                    servicer.AddSamples,
                    request_deserializer=xk6__output__plugin__py_dot_output__pb2.AddSamplesRequest.FromString,
                    response_serializer=xk6__output__plugin__py_dot_output__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'xk6_output_plugin.output.Output', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Output(object):
    """Output is the gRPC service to be implemented by output plugins.
    """

    @staticmethod
    def Init(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/xk6_output_plugin.output.Output/Init',
            xk6__output__plugin__py_dot_output__pb2.InitRequest.SerializeToString,
            xk6__output__plugin__py_dot_output__pb2.InitResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Start(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/xk6_output_plugin.output.Output/Start',
            xk6__output__plugin__py_dot_output__pb2.Empty.SerializeToString,
            xk6__output__plugin__py_dot_output__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Stop(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/xk6_output_plugin.output.Output/Stop',
            xk6__output__plugin__py_dot_output__pb2.Empty.SerializeToString,
            xk6__output__plugin__py_dot_output__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddMetrics(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/xk6_output_plugin.output.Output/AddMetrics',
            xk6__output__plugin__py_dot_output__pb2.AddMetricsRequest.SerializeToString,
            xk6__output__plugin__py_dot_output__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddSamples(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/xk6_output_plugin.output.Output/AddSamples',
            xk6__output__plugin__py_dot_output__pb2.AddSamplesRequest.SerializeToString,
            xk6__output__plugin__py_dot_output__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)