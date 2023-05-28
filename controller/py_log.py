INFO:sqlalchemy.engine.Engine:select pg_catalog.version()
INFO:sqlalchemy.engine.Engine:[raw sql] {}
INFO:sqlalchemy.engine.Engine:select current_schema()
INFO:sqlalchemy.engine.Engine:[raw sql] {}
INFO:sqlalchemy.engine.Engine:show standard_conforming_strings
INFO:sqlalchemy.engine.Engine:[raw sql] {}
WARNING:werkzeug: * Debugger is active!
INFO:werkzeug: * Debugger PIN: 124-178-072
ERROR:root:When initializing mapper Mapper[OrderHeader(order_header)], expression 'OrderItem' failed to locate a name ('OrderItem'). If this is a class name, consider adding this reINFO:werkzeug: * Restarting with stat
_entity.OrderHeader'> class after both dependent classes have been defined.
Traceback (most recent call last):
  File "/Users/olegtetenev/PycharmProjects/iShop_App/venv/lib/python3.11/site-packages/sqlalchemy/orm/clsregistry.py", line 515, in _resolve_name
    rval = d[token]
           ~^^^^^^^
  File "/Users/olegtetenev/PycharmProjects/iShop_App/venv/lib/python3.11/site-packages/sqlalchemy/util/_collections.py", line 346, in __missing__
    self[key] = val = self.creator(key)
                      ^^^^^^^^^^^^^^^^^
  File "/Users/olegtetenev/PycharmProjects/iShop_App/venv/lib/python3.11/site-packages/sqlalchemy/orm/clsregistry.py", line 483, in _access_cls
    return self.fallback[key]
           ~~~~~~~~~~~~~^^^^^
KeyError: 'OrderItem'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/Users/olegtetenev/PycharmProjects/iShop_App/controller/order_handler.py", line 38, in get
    order_data = order_srv.get(order_id)
                 ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/olegtetenev/PycharmProjects/iShop_App/business/order_service.py", line 13, in get
    order_dataclass = self._order_repo.read_one(order_id)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/olegtetenev/PycharmProjects/iShop_App/repository/order_repository.py", line 38, in read_one
    data = curr_session.query(OrderHeader).get(order_id)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/olegtetenev/PycharmProjects/iShop_App/venv/lib/python3.11/site-packages/sqlalchemy/orm/session.py", line 2799, in query
    return self._query_cls(entities, self, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/olegtetenev/PycharmProjects/iShop_App/venv/lib/python3.11/site-packages/sqlalchemy/orm/query.py", line 273, in __init__
    self._set_entities(entities)
  File "/Users/olegtetenev/PycharmProjects/iShop_App/venv/lib/python3.11/site-packages/sqlalchemy/orm/query.py", line 282, in _set_entities
    self._raw_columns = [
                        ^
  File "/Users/olegtetenev/PycharmProjects/iShop_App/venv/lib/python3.11/site-packages/sqlalchemy/orm/query.py", line 283, in <listcomp>
    coercions.expect(
  File "/Users/olegtetenev/PycharmProjects/iShop_App/venv/lib/python3.11/site-packages/sqlalchemy/sql/coercions.py", line 406, in expect
    insp._post_inspect
  File "/Users/olegtetenev/PycharmProjects/iShop_App/venv/lib/python3.11/site-packages/sqlalchemy/util/langhelpers.py", line 1257, in __get__
    obj.__dict__[self.__name__] = result = self.fget(obj)
                                           ^^^^^^^^^^^^^^
  File "/Users/olegtetenev/PycharmProjects/iShop_App/venv/lib/python3.11/site-packages/sqlalchemy/orm/mapper.py", line 2681, in _post_inspect
    self._check_configure()
  File "/Users/olegtetenev/PycharmProjects/iShop_App/venv/lib/python3.11/site-packages/sqlalchemy/orm/mapper.py", line 2362, in _check_configure
    _configure_registries({self.registry}, cascade=True)
  File "/Users/olegtetenev/PycharmProjects/iShop_App/venv/lib/python3.11/site-packages/sqlalchemy/orm/mapper.py", line 4177, in _configure_registries
    _do_configure_registries(registries, cascade)
  File "/Users/olegtetenev/PycharmProjects/iShop_App/venv/lib/python3.11/site-packages/sqlalchemy/orm/mapper.py", line 4219, in _do_configure_registries
    mapper._post_configure_properties()
  File "/Users/olegtetenev/PycharmProjects/iShop_App/venv/lib/python3.11/site-packages/sqlalchemy/orm/mapper.py", line 2379, in _post_configure_properties
    prop.init()
  File "/Users/olegtetenev/PycharmProjects/iShop_App/venv/lib/python3.11/site-packages/sqlalchemy/orm/interfaces.py", line 549, in init
    self.do_init()
  File "/Users/olegtetenev/PycharmProjects/iShop_App/venv/lib/python3.11/site-packages/sqlalchemy/orm/relationships.py", line 1632, in do_init
    self._setup_entity()
  File "/Users/olegtetenev/PycharmProjects/iShop_App/venv/lib/python3.11/site-packages/sqlalchemy/orm/relationships.py", line 1851, in _setup_entity
    self._clsregistry_resolve_name(argument)(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/olegtetenev/PycharmProjects/iShop_App/venv/lib/python3.11/site-packages/sqlalchemy/orm/clsregistry.py", line 519, in _resolve_name
    self._raise_for_name(name, err)
  File "/Users/olegtetenev/PycharmProjects/iShop_App/venv/lib/python3.11/site-packages/sqlalchemy/orm/clsregistry.py", line 500, in _raise_for_name
    raise exc.InvalidRequestError(
sqlalchemy.exc.InvalidRequestError: When initializing mapper Mapper[OrderHeader(order_header)], expression 'OrderItem' failed to locate a name ('OrderItem'). If this is a class name, consider adding this relationship() to the <class 'order_repo_entity.OrderHeader'> class after both dependent classes have been defined.
INFO:werkzeug:127.0.0.1 - - [28/May/2023 15:49:22] "[35m[1mGET /api/order/5 HTTP/1.1[0m" 500 -
INFO:werkzeug: * Detected change in '/Users/olegtetenev/PycharmProjects/iShop_App/controller/py_log.py', reloading
