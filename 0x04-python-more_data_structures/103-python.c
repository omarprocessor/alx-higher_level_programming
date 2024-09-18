#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Print basic info about a Python list object
 * @p: Python object
 */
void print_python_list(PyObject *p)
{
Py_ssize_t i, size;
PyObject *item;

if (!PyList_Check(p))
{
printf("[*] Error: Invalid List Object\n");
return;
}

size = PyList_Size(p);
printf("[*] Python list info\n");
printf("[*] Size of the Python List = %zd\n", size);
printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

for (i = 0; i < size; i++)
{
item = PyList_GetItem(p, i);
printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
if (PyBytes_Check(item))
{
printf("[.] bytes object info\n");
printf("  size: %zd\n", PyBytes_Size(item));
printf("  trying string: %s\n", PyBytes_AsString(item));
printf("  first %zd bytes: ", (PyBytes_Size(item) > 10) ? 10 : PyBytes_Size(item));
for (Py_ssize_t j = 0; j < (PyBytes_Size(item) > 10 ? 10 : PyBytes_Size(item)); j++)
printf("%02x ", (unsigned char)PyBytes_AsString(item)[j]);
printf("\n");
}
}
}
