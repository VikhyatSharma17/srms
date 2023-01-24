superuser:
    Username: admin
    Password: Admin#123
    Email: admin@srms.com


## Design Inspirations:
- https://www.uplabs.com/posts/education-dashboard-001e79a5-5d56-4d89-8cd4-dbc325a5210d
- https://www.uplabs.com/posts/online-education-dashboard-ui-97252eb1-a87d-4a6f-9417-499e3f9464ff
- https://icons8.com/illustrations/illustration/taxi-online-education-3


>>> def multipliers():
...     return [lambda x, i=i: i*x for i in range(4)]
...
>>> print([m(2) for m in multipliers()])
[0, 2, 4, 6]
