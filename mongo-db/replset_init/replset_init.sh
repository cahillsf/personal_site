#!/bin/sh
mongod --shutdown && mongod --bind_ip 0.0.0.0 --replSet MainRepSet