# coding: utf-8
#
# Copyright 2014 The Oppia Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, softwar
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Rules for ListOfUnicodeString objects."""

__author__ = 'Sean Lip'

from extensions.rules import base


class Equals(base.ListOfUnicodeStringRule):
    description = 'is equal to {{x|ListOfUnicodeString}}'
    is_generic = False

    def _evaluate(self, subject):
        return subject == self.x


class IsLongerThan(base.ListOfUnicodeStringRule):
    description = 'has more than {{k|NonnegativeInt}} elements'
    is_generic = True

    def _evaluate(self, subject):
        return len(subject) > self.k


class HasLengthInclusivelyBetween(base.ListOfUnicodeStringRule):
    description = ('has between {{a|NonnegativeInt}} and '
                   '{{b|NonnegativeInt}} elements, inclusive')
    is_generic = True

    def _validate_params(self):
        assert self.a <= self.b

    def _evaluate(self, subject):
        return self.a <= len(subject) <= self.b


class EqualsElementWise(base.ListOfUnicodeStringRule):
    description = (
        'has an element at index {{k|NonnegativeInt}} that is equal to '
        '{{x|UnicodeString}}')
    is_generic = True

    def _evaluate(self, subject):
        return len(subject) > self.k and subject[self.k] == self.x


class HasElementsIn(base.ListOfUnicodeStringRule):
    description = 'has elements in common with {{x|SetOfUnicodeString}}'
    is_generic = True

    def _evaluate(self, subject):
        return bool(set(subject).intersection(set(self.x)))


class HasElementsNotIn(base.ListOfUnicodeStringRule):
    description = 'has elements not in {{x|SetOfUnicodeString}}'
    is_generic = True

    def _evaluate(self, subject):
        return bool(set(subject) - set(self.x))


class OmitsElementsIn(base.ListOfUnicodeStringRule):
    description = 'omits some elements of {{x|SetOfUnicodeString}}'
    is_generic = True

    def _evaluate(self, subject):
        return bool(set(self.x) - set(subject))


class IsDisjointFrom(base.ListOfUnicodeStringRule):
    description = 'has no elements in common with {{x|SetOfUnicodeString}}'
    is_generic = True

    def _evaluate(self, subject):
        return not bool(set(subject).intersection(set(self.x)))