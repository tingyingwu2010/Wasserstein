# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import itertools
import numpy as np



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _wasserstein
else:
    import _wasserstein

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _wasserstein.SWIG_PyInstanceMethod_New
_swig_new_static_method = _wasserstein.SWIG_PyStaticMethod_New

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _wasserstein.delete_SwigPyIterator
    value = _swig_new_instance_method(_wasserstein.SwigPyIterator_value)
    incr = _swig_new_instance_method(_wasserstein.SwigPyIterator_incr)
    decr = _swig_new_instance_method(_wasserstein.SwigPyIterator_decr)
    distance = _swig_new_instance_method(_wasserstein.SwigPyIterator_distance)
    equal = _swig_new_instance_method(_wasserstein.SwigPyIterator_equal)
    copy = _swig_new_instance_method(_wasserstein.SwigPyIterator_copy)
    next = _swig_new_instance_method(_wasserstein.SwigPyIterator_next)
    __next__ = _swig_new_instance_method(_wasserstein.SwigPyIterator___next__)
    previous = _swig_new_instance_method(_wasserstein.SwigPyIterator_previous)
    advance = _swig_new_instance_method(_wasserstein.SwigPyIterator_advance)
    __eq__ = _swig_new_instance_method(_wasserstein.SwigPyIterator___eq__)
    __ne__ = _swig_new_instance_method(_wasserstein.SwigPyIterator___ne__)
    __iadd__ = _swig_new_instance_method(_wasserstein.SwigPyIterator___iadd__)
    __isub__ = _swig_new_instance_method(_wasserstein.SwigPyIterator___isub__)
    __add__ = _swig_new_instance_method(_wasserstein.SwigPyIterator___add__)
    __sub__ = _swig_new_instance_method(_wasserstein.SwigPyIterator___sub__)
    def __iter__(self):
        return self

# Register SwigPyIterator in _wasserstein:
_wasserstein.SwigPyIterator_swigregister(SwigPyIterator)

class vectorDouble(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    iterator = _swig_new_instance_method(_wasserstein.vectorDouble_iterator)
    def __iter__(self):
        return self.iterator()
    __nonzero__ = _swig_new_instance_method(_wasserstein.vectorDouble___nonzero__)
    __bool__ = _swig_new_instance_method(_wasserstein.vectorDouble___bool__)
    __len__ = _swig_new_instance_method(_wasserstein.vectorDouble___len__)
    __getslice__ = _swig_new_instance_method(_wasserstein.vectorDouble___getslice__)
    __setslice__ = _swig_new_instance_method(_wasserstein.vectorDouble___setslice__)
    __delslice__ = _swig_new_instance_method(_wasserstein.vectorDouble___delslice__)
    __delitem__ = _swig_new_instance_method(_wasserstein.vectorDouble___delitem__)
    __getitem__ = _swig_new_instance_method(_wasserstein.vectorDouble___getitem__)
    __setitem__ = _swig_new_instance_method(_wasserstein.vectorDouble___setitem__)
    pop = _swig_new_instance_method(_wasserstein.vectorDouble_pop)
    append = _swig_new_instance_method(_wasserstein.vectorDouble_append)
    empty = _swig_new_instance_method(_wasserstein.vectorDouble_empty)
    size = _swig_new_instance_method(_wasserstein.vectorDouble_size)
    swap = _swig_new_instance_method(_wasserstein.vectorDouble_swap)
    begin = _swig_new_instance_method(_wasserstein.vectorDouble_begin)
    end = _swig_new_instance_method(_wasserstein.vectorDouble_end)
    rbegin = _swig_new_instance_method(_wasserstein.vectorDouble_rbegin)
    rend = _swig_new_instance_method(_wasserstein.vectorDouble_rend)
    clear = _swig_new_instance_method(_wasserstein.vectorDouble_clear)
    get_allocator = _swig_new_instance_method(_wasserstein.vectorDouble_get_allocator)
    pop_back = _swig_new_instance_method(_wasserstein.vectorDouble_pop_back)
    erase = _swig_new_instance_method(_wasserstein.vectorDouble_erase)

    def __init__(self, *args):
        _wasserstein.vectorDouble_swiginit(self, _wasserstein.new_vectorDouble(*args))
    push_back = _swig_new_instance_method(_wasserstein.vectorDouble_push_back)
    front = _swig_new_instance_method(_wasserstein.vectorDouble_front)
    back = _swig_new_instance_method(_wasserstein.vectorDouble_back)
    assign = _swig_new_instance_method(_wasserstein.vectorDouble_assign)
    resize = _swig_new_instance_method(_wasserstein.vectorDouble_resize)
    insert = _swig_new_instance_method(_wasserstein.vectorDouble_insert)
    reserve = _swig_new_instance_method(_wasserstein.vectorDouble_reserve)
    capacity = _swig_new_instance_method(_wasserstein.vectorDouble_capacity)
    __swig_destroy__ = _wasserstein.delete_vectorDouble

# Register vectorDouble in _wasserstein:
_wasserstein.vectorDouble_swigregister(vectorDouble)

class vectorString(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    iterator = _swig_new_instance_method(_wasserstein.vectorString_iterator)
    def __iter__(self):
        return self.iterator()
    __nonzero__ = _swig_new_instance_method(_wasserstein.vectorString___nonzero__)
    __bool__ = _swig_new_instance_method(_wasserstein.vectorString___bool__)
    __len__ = _swig_new_instance_method(_wasserstein.vectorString___len__)
    __getslice__ = _swig_new_instance_method(_wasserstein.vectorString___getslice__)
    __setslice__ = _swig_new_instance_method(_wasserstein.vectorString___setslice__)
    __delslice__ = _swig_new_instance_method(_wasserstein.vectorString___delslice__)
    __delitem__ = _swig_new_instance_method(_wasserstein.vectorString___delitem__)
    __getitem__ = _swig_new_instance_method(_wasserstein.vectorString___getitem__)
    __setitem__ = _swig_new_instance_method(_wasserstein.vectorString___setitem__)
    pop = _swig_new_instance_method(_wasserstein.vectorString_pop)
    append = _swig_new_instance_method(_wasserstein.vectorString_append)
    empty = _swig_new_instance_method(_wasserstein.vectorString_empty)
    size = _swig_new_instance_method(_wasserstein.vectorString_size)
    swap = _swig_new_instance_method(_wasserstein.vectorString_swap)
    begin = _swig_new_instance_method(_wasserstein.vectorString_begin)
    end = _swig_new_instance_method(_wasserstein.vectorString_end)
    rbegin = _swig_new_instance_method(_wasserstein.vectorString_rbegin)
    rend = _swig_new_instance_method(_wasserstein.vectorString_rend)
    clear = _swig_new_instance_method(_wasserstein.vectorString_clear)
    get_allocator = _swig_new_instance_method(_wasserstein.vectorString_get_allocator)
    pop_back = _swig_new_instance_method(_wasserstein.vectorString_pop_back)
    erase = _swig_new_instance_method(_wasserstein.vectorString_erase)

    def __init__(self, *args):
        _wasserstein.vectorString_swiginit(self, _wasserstein.new_vectorString(*args))
    push_back = _swig_new_instance_method(_wasserstein.vectorString_push_back)
    front = _swig_new_instance_method(_wasserstein.vectorString_front)
    back = _swig_new_instance_method(_wasserstein.vectorString_back)
    assign = _swig_new_instance_method(_wasserstein.vectorString_assign)
    resize = _swig_new_instance_method(_wasserstein.vectorString_resize)
    insert = _swig_new_instance_method(_wasserstein.vectorString_insert)
    reserve = _swig_new_instance_method(_wasserstein.vectorString_reserve)
    capacity = _swig_new_instance_method(_wasserstein.vectorString_capacity)
    __swig_destroy__ = _wasserstein.delete_vectorString

# Register vectorString in _wasserstein:
_wasserstein.vectorString_swigregister(vectorString)

Success = _wasserstein.Success
Empty = _wasserstein.Empty
SupplyMismatch = _wasserstein.SupplyMismatch
Unbounded = _wasserstein.Unbounded
MaxIterReached = _wasserstein.MaxIterReached
Infeasible = _wasserstein.Infeasible
ExtraParticle_Neither = _wasserstein.ExtraParticle_Neither
ExtraParticle_Zero = _wasserstein.ExtraParticle_Zero
ExtraParticle_One = _wasserstein.ExtraParticle_One
class ExternalEMDHandler(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _wasserstein.delete_ExternalEMDHandler
    __call__ = _swig_new_instance_method(_wasserstein.ExternalEMDHandler___call__)
    description = _swig_new_instance_method(_wasserstein.ExternalEMDHandler_description)

# Register ExternalEMDHandler in _wasserstein:
_wasserstein.ExternalEMDHandler_swigregister(ExternalEMDHandler)

class Histogram1DHandler(ExternalEMDHandler):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _wasserstein.Histogram1DHandler_swiginit(self, _wasserstein.new_Histogram1DHandler(*args))
    __swig_destroy__ = _wasserstein.delete_Histogram1DHandler
    description = _swig_new_instance_method(_wasserstein.Histogram1DHandler_description)
    bin_centers = _swig_new_instance_method(_wasserstein.Histogram1DHandler_bin_centers)
    bin_edges = _swig_new_instance_method(_wasserstein.Histogram1DHandler_bin_edges)
    hist_vals_errs = _swig_new_instance_method(_wasserstein.Histogram1DHandler_hist_vals_errs)
    print_axis = _swig_new_instance_method(_wasserstein.Histogram1DHandler_print_axis)
    print_hist = _swig_new_instance_method(_wasserstein.Histogram1DHandler_print_hist)

# Register Histogram1DHandler in _wasserstein:
_wasserstein.Histogram1DHandler_swigregister(Histogram1DHandler)

class Histogram1DHandlerLog(ExternalEMDHandler):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _wasserstein.Histogram1DHandlerLog_swiginit(self, _wasserstein.new_Histogram1DHandlerLog(*args))
    __swig_destroy__ = _wasserstein.delete_Histogram1DHandlerLog
    description = _swig_new_instance_method(_wasserstein.Histogram1DHandlerLog_description)
    bin_centers = _swig_new_instance_method(_wasserstein.Histogram1DHandlerLog_bin_centers)
    bin_edges = _swig_new_instance_method(_wasserstein.Histogram1DHandlerLog_bin_edges)
    hist_vals_errs = _swig_new_instance_method(_wasserstein.Histogram1DHandlerLog_hist_vals_errs)
    print_axis = _swig_new_instance_method(_wasserstein.Histogram1DHandlerLog_print_axis)
    print_hist = _swig_new_instance_method(_wasserstein.Histogram1DHandlerLog_print_hist)

# Register Histogram1DHandlerLog in _wasserstein:
_wasserstein.Histogram1DHandlerLog_swigregister(Histogram1DHandlerLog)

class CorrelationDimension(Histogram1DHandlerLog):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _wasserstein.CorrelationDimension_swiginit(self, _wasserstein.new_CorrelationDimension(*args))
    __swig_destroy__ = _wasserstein.delete_CorrelationDimension
    cumulative_vals_vars = _swig_new_instance_method(_wasserstein.CorrelationDimension_cumulative_vals_vars)
    corrdims = _swig_new_instance_method(_wasserstein.CorrelationDimension_corrdims)
    corrdim_bins = _swig_new_instance_method(_wasserstein.CorrelationDimension_corrdim_bins)

# Register CorrelationDimension in _wasserstein:
_wasserstein.CorrelationDimension_swigregister(CorrelationDimension)

class EMDArrayEuclidean(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, R: "double"=1, beta: "double"=1, norm: "bool"=False, do_timing: "bool"=False, n_iter_max: "unsigned int"=100000, epsilon_large_factor: "double"=10000, epsilon_small_factor: "double"=0):
        _wasserstein.EMDArrayEuclidean_swiginit(self, _wasserstein.new_EMDArrayEuclidean(R, beta, norm, do_timing, n_iter_max, epsilon_large_factor, epsilon_small_factor))
    __swig_destroy__ = _wasserstein.delete_EMDArrayEuclidean
    description = _swig_new_instance_method(_wasserstein.EMDArrayEuclidean_description)
    network_simplex = _swig_new_instance_method(_wasserstein.EMDArrayEuclidean_network_simplex)
    pairwise_distance = _swig_new_instance_method(_wasserstein.EMDArrayEuclidean_pairwise_distance)
    clear = _swig_new_instance_method(_wasserstein.EMDArrayEuclidean_clear)
    extra = _swig_new_instance_method(_wasserstein.EMDArrayEuclidean_extra)
    n0 = _swig_new_instance_method(_wasserstein.EMDArrayEuclidean_n0)
    n1 = _swig_new_instance_method(_wasserstein.EMDArrayEuclidean_n1)
    dists_vec = _swig_new_instance_method(_wasserstein.EMDArrayEuclidean_dists_vec)
    emd = _swig_new_instance_method(_wasserstein.EMDArrayEuclidean_emd)
    status = _swig_new_instance_method(_wasserstein.EMDArrayEuclidean_status)
    flow = _swig_new_instance_method(_wasserstein.EMDArrayEuclidean_flow)
    flows_vec = _swig_new_instance_method(_wasserstein.EMDArrayEuclidean_flows_vec)
    duration = _swig_new_instance_method(_wasserstein.EMDArrayEuclidean_duration)
    __str__ = _swig_new_instance_method(_wasserstein.EMDArrayEuclidean___str__)
    flows = _swig_new_instance_method(_wasserstein.EMDArrayEuclidean_flows)
    dists = _swig_new_instance_method(_wasserstein.EMDArrayEuclidean_dists)
    __call__ = _swig_new_instance_method(_wasserstein.EMDArrayEuclidean___call__)

# Register EMDArrayEuclidean in _wasserstein:
_wasserstein.EMDArrayEuclidean_swigregister(EMDArrayEuclidean)

class EMDArray(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, R: "double"=1, beta: "double"=1, norm: "bool"=False, do_timing: "bool"=False, n_iter_max: "unsigned int"=100000, epsilon_large_factor: "double"=10000, epsilon_small_factor: "double"=0):
        _wasserstein.EMDArray_swiginit(self, _wasserstein.new_EMDArray(R, beta, norm, do_timing, n_iter_max, epsilon_large_factor, epsilon_small_factor))
    __swig_destroy__ = _wasserstein.delete_EMDArray
    description = _swig_new_instance_method(_wasserstein.EMDArray_description)
    network_simplex = _swig_new_instance_method(_wasserstein.EMDArray_network_simplex)
    pairwise_distance = _swig_new_instance_method(_wasserstein.EMDArray_pairwise_distance)
    clear = _swig_new_instance_method(_wasserstein.EMDArray_clear)
    extra = _swig_new_instance_method(_wasserstein.EMDArray_extra)
    n0 = _swig_new_instance_method(_wasserstein.EMDArray_n0)
    n1 = _swig_new_instance_method(_wasserstein.EMDArray_n1)
    dists_vec = _swig_new_instance_method(_wasserstein.EMDArray_dists_vec)
    emd = _swig_new_instance_method(_wasserstein.EMDArray_emd)
    status = _swig_new_instance_method(_wasserstein.EMDArray_status)
    flow = _swig_new_instance_method(_wasserstein.EMDArray_flow)
    flows_vec = _swig_new_instance_method(_wasserstein.EMDArray_flows_vec)
    duration = _swig_new_instance_method(_wasserstein.EMDArray_duration)
    __str__ = _swig_new_instance_method(_wasserstein.EMDArray___str__)
    flows = _swig_new_instance_method(_wasserstein.EMDArray_flows)
    dists = _swig_new_instance_method(_wasserstein.EMDArray_dists)
    __call__ = _swig_new_instance_method(_wasserstein.EMDArray___call__)

# Register EMDArray in _wasserstein:
_wasserstein.EMDArray_swigregister(EMDArray)

class PairwiseEMDArrayEuclidean(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args, **kwargs):
        _wasserstein.PairwiseEMDArrayEuclidean_swiginit(self, _wasserstein.new_PairwiseEMDArrayEuclidean(*args, **kwargs))
    __swig_destroy__ = _wasserstein.delete_PairwiseEMDArrayEuclidean
    description = _swig_new_instance_method(_wasserstein.PairwiseEMDArrayEuclidean_description)
    set_omp_dynamic_chunksize = _swig_new_instance_method(_wasserstein.PairwiseEMDArrayEuclidean_set_omp_dynamic_chunksize)
    set_external_emd_handler = _swig_new_instance_method(_wasserstein.PairwiseEMDArrayEuclidean_set_external_emd_handler)

    def clear(self):
        _wasserstein.PairwiseEMDArrayEuclidean_clear(self)
        self.event_arrs = []


    emd = _swig_new_instance_method(_wasserstein.PairwiseEMDArrayEuclidean_emd)
    emds_vec = _swig_new_instance_method(_wasserstein.PairwiseEMDArrayEuclidean_emds_vec)
    errored = _swig_new_instance_method(_wasserstein.PairwiseEMDArrayEuclidean_errored)
    error_messages = _swig_new_instance_method(_wasserstein.PairwiseEMDArrayEuclidean_error_messages)
    report_errors = _swig_new_instance_method(_wasserstein.PairwiseEMDArrayEuclidean_report_errors)
    num_emds = _swig_new_instance_method(_wasserstein.PairwiseEMDArrayEuclidean_num_emds)
    nevA = _swig_new_instance_method(_wasserstein.PairwiseEMDArrayEuclidean_nevA)
    nevB = _swig_new_instance_method(_wasserstein.PairwiseEMDArrayEuclidean_nevB)
    init = _swig_new_instance_method(_wasserstein.PairwiseEMDArrayEuclidean_init)
    compute = _swig_new_instance_method(_wasserstein.PairwiseEMDArrayEuclidean_compute)
    __str__ = _swig_new_instance_method(_wasserstein.PairwiseEMDArrayEuclidean___str__)
    _add_event = _swig_new_instance_method(_wasserstein.PairwiseEMDArrayEuclidean__add_event)
    npy_emds = _swig_new_instance_method(_wasserstein.PairwiseEMDArrayEuclidean_npy_emds)

    def __call__(self, events0, events1=None, gdim=None):

        if events1 is None:
            self.init(len(events0))
            events1 = []
        else:
            self.init(len(events0), len(events1))

        self.event_arrs = []
        for event in itertools.chain(events0, events1):

    # extract weights and coords from 
            event = np.atleast_2d(event)
            weights = np.ascontiguousarray(event[:,0], dtype=np.double)
            coords = np.ascontiguousarray(event[:,1:] if gdim is None else event[:,1:gdim+1])

    # ensure that the lifetime of these arrays lasts through the computation
            self.event_arrs.append((weights, coords))

    # store individual event
            self._add_event(weights, coords)

    # run actual computation
        self.compute()


# Register PairwiseEMDArrayEuclidean in _wasserstein:
_wasserstein.PairwiseEMDArrayEuclidean_swigregister(PairwiseEMDArrayEuclidean)



