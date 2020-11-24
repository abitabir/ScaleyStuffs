"""
User defined data structures: dictionary. [Uhhh... kinda?]
"""

class MarksDistribution:

    def __init__(self, marks=[], max=100, min=0):
        if max <= min:
            raise ValueError
        self._marks = marks
        self._max = max
        self._min = min

    def add_all(self, student_marks):
        """
        Method adds all integer values in list inputted to the instance of MarkDistribution's _marks attribute (note:
        which may not be empty). Raises ValueError if an integer value is outside max-min range defined upon
        initialisation.
        """
        for mark in student_marks:
            if mark < self._min or mark > self._max:
                raise ValueError
            self._marks.append(mark)
        return


    def get_distribution(self, bins):
        """
        Returns histogram bars and their weights in an abstract programming data structure format - list of tuples, but
        raising ValueError if range of marks is not divisible by input.
        :param bins: An integer corresponding to the number of bars (bins) to be displayed in the distribution.
        :return: A list of tuples in ascending order of ranges of marks. A tuple contains the label of that bin and the
        corresponding number of marks in that bin.
        """


        def messy():
            for i in range(len(self._marks)):
                if self._marks[i] % bins == 0:
                    if i != 0:
                        bin_range_of_marks += str(i)
                        output.append((bin_range_of_marks, count))
                    bin_range_of_marks = str(i) + "-"
                    count = self._marks[i]
                else:
                    count += self._marks[i]
            return output


        def very_confusion_I(hum):
            binthile_boundaries = finding_boundaries(range_of_marks, bins)
            binned_split = split_by_boundaries(self._marks, bins, binthile_boundaries)
            for bin_index in range(len(binned_split)):
                bin_range = str(bin_index * bins) + "-" + str((bin_index * (bins + 1)) - 1)
                bin_count = 0
                for mark in binned_split[bin_index]:
                    bin_count += 1
                output.append((bin_range, bin_count))
                print(bin_index, bin_range, bin_count)
            return output

        def messy_split_by_splitting(listo, splittingo):
            list_of_lists = []
            for indexo in range(len(listo)):
                if indexo % splittingo == 0:
                    if indexo != 0:
                        list_of_lists.append(thingy)
                    thingy = [listo[indexo]]
                else:
                    thingy.append(listo[indexo])
            return list_of_lists


        def finding_boundaries(min, max, range_of_marks, bins):
            binthile_boundaries = []
            for binthile_boundary in range(min, max + 1, int(range_of_marks/bins)):
                # gives smallest to largest nthiles possible ~ stepping per bin
                binthile_boundaries.append(binthile_boundary)
            return binthile_boundaries


        def countings_by_boundaries_range(all_marks, bins, binthile_boundaries):  # not very efficient tbf but first one to WORK
            output = []
            all_marks.sort()  # no guarantee that the attribute is arranged ascendingly XOOO
            for boundary_index in range(1, len(binthile_boundaries) + 1):
                bin_count = 0
                bin_range = str(binthile_boundaries[boundary_index - 1]) + "-" + str(binthile_boundaries[boundary_index - 1] + bins)
                for mark in all_marks:
                    if mark >= binthile_boundaries[boundary_index - 1] and mark < binthile_boundaries[boundary_index]:
                        bin_count += 1
                output.append((bin_range, bin_count))
            return output

        def countings_by_boundaries_range_better(all_marks, bins, range_of_marks,
                                                 binthile_boundaries):  # aspirationally aiming to be more efficient
            # than first one to work by not doing unnecessary iteration through logicallnesses
            # to be fair. could have just made binthile_boundaries into a dico... would have been much easier, but I am sick of this question now lol
            # no need to go through EVERY iteration for EVERY iteration in nested for loop, if we know _things_
            output = []
            all_marks.sort()  # no guarantee that the attribute is arranged ascendingly XOOO
            boundary_index = 0
            mark_index = 0
            continueLoop = True  # while True
            while continueLoop:  # was mark_index < len(all_marks) and boundary_index < len(
                # binthile_boundaries) + 1:  # only 1/binth a nested loop I think
                # if mark greater than maximum won't be able to iterate further with this loop
                if all_marks[mark_index] >= binthile_boundaries[boundary_index]:  # time for savings and resettings
                    # if mark is greater than the boundary we are innn
                    # but condition throws error if mark_index or boundary_index out of list index range so after
                    # iteration conditions at bottom of while loop
                    if binthile_boundaries[boundary_index] != binthile_boundaries[0]:
                        bin_range = str(binthile_boundaries[boundary_index - 1]) + "-" + str(
                            binthile_boundaries[boundary_index - 1] + int(range_of_marks / bins) - 1)
                        output.append((bin_range,
                                       bin_count))  # order matters, for when boundary_index == 1, the first variable may not even exist!
                    # need the rest of all this to happen even if first iteration with boundary_index being 0 ~ initialising these variables
                    boundary_index += 1
                    bin_count = 0
                bin_count += 1
                mark_index += 1
                # conditions checking if in bounds after new iteration variables set
                if mark_index >= len(all_marks) and boundary_index > len(binthile_boundaries):
                    continueLoop = False
                elif mark_index == len(all_marks) - 1:
                    # was incorrectly binthile_boundaries[boundary_index] == binthile_boundaries[-1]
                    # ~ for last iteration savings before lost
                    bin_count += 1  # to add last iteration count, special exception deviating from the normal addition way cuz index out of bounds
                    bin_range = str(binthile_boundaries[boundary_index - 1]) + "-" + str(
                        binthile_boundaries[boundary_index - 1] + int(range_of_marks / bins))
                    print((bin_range, bin_count))
                    output.append((bin_range, bin_count))
                    continueLoop = False
            return output

        range_of_marks = self._max - self._min
        if range_of_marks % bins != 0:
            raise ValueError
        output = []
        binthile_boundaries = finding_boundaries(self._min, self._max, range_of_marks, bins)
        # binned_split = countings_by_boundaries_range(self._marks, bins, binthile_boundaries)
        binned_split = countings_by_boundaries_range_better(self._marks, bins, range_of_marks, binthile_boundaries)
        return binned_split


ExamResults = MarksDistribution()
ExamResults.add_all([15, 56, 78, 45, 78, 54])
print(ExamResults._marks)
print(ExamResults.get_distribution(4))
