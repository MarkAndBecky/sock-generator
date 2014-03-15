__author__ = 'becky'


#!/usr/bin/env python
# -*- coding: utf-8 -*-




def gauge(units, stitches, rows):
    """
    Calculates row and stich guage per inch or per cm based on rows and stitches per 4 inches or 10 cm.
    """
    inches = ["inches", "inch", "in", "ins", '"']
    cm = ["centimetres", "centimeters", "cm", "cms"]
    if units.lower() in inches:
        st_gauge = float(stitches) / 4
        r_gauge = float(rows) / 4
        unit_used = "inches"
        return r_gauge, st_gauge, unit_used
    elif units.lower() in cm:
        st_gauge = float(stitches) / 10
        r_gauge = float(rows) / 10
        unit_used = "cms"
        return r_gauge, st_gauge, unit_used
    else:
        print "Units '%s' not recognised" % units


def cast_on_stitches(st_gauge, foot_circum, ease):
    """
    Calculates number of stitches to provisionally cast on to start short row toe.
    Ease should be entered as a percentage, negative or positive (-10 is usual).
    """
    sock_circum = float(foot_circum) + (float(foot_circum) * (float(ease)/100))
    cast_on = round((float(sock_circum) * st_gauge) / 2)
    #print "Foot circumference: %.2f\nSock circumference: %.2f\nCast on for toe: %.2f" % \
    #      (float(foot_circum), sock_circum, cast_on)
    return cast_on



def short_row_end_stitches(start_stitches, percent):
    """
    Calcuates number of stitches at end of short row toe; this number is even if the number of toe stitches is even,
    and odd if the number of toe stitches is odd.
    """

    x = round(float(start_stitches) * percent)

    if float(start_stitches) % 2 == 0:  # if starting stitches are an odd number
        if x % 2 == 0:
            return x
        else:
            if x > (float(start_stitches) * percent):
                return x - 1
            else:
                return x + 1
    else:  # if starting stitches are an odd number
        if x % 2 == 0:
            if x >= (float(start_stitches) * percent):
                return x + 1
            else:
                return x - 1
        else:
            return x

def short_row_end_test():
    print "Test short row end sts:"
    toe_stitch_list = [22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
    for i in toe_stitch_list:
        print "Toe stitches: ", i, "; toe end sts: ", short_row_end_stitches(int(i), 0.3)
        print "Heel stitches: ", i, "; heel end sts: ", short_row_end_stitches(int(i), 0.4)


def short_row_length(start_stitches, end_stitches, rgauge):
    """
    Calculate length of the short row toe or heel.
    """
    short_rows = start_stitches - end_stitches
    sr_length = short_rows / rgauge
    return sr_length


def get_input():
    """
    Obtain the user input values.
    """
    input_units = raw_input("Units (inch/cm):")
    swatch_stitches = float(raw_input("Stitches per 10cm/4in:"))
    swatch_rows = float(raw_input("Rows per 10sm/4in:"))
    foot_circum = float(raw_input("Foot circumference in %s at widest point:" % input_units))
    foot_length = float(raw_input("Foot length in %s:" % input_units))
    ease = float(raw_input("Ease required in % (standard is -10):"))

    return input_units, swatch_stitches, swatch_rows, foot_circum, foot_length, ease

def pattern():

    input_units, swatch_stitches, swatch_rows, foot_circum, foot_length, ease = get_input()
    rgauge, stgauge, units = gauge(input_units, swatch_stitches, swatch_rows)
    cast_on = cast_on_stitches(stgauge, foot_circum, ease)
    heel_end = short_row_end_stitches(cast_on, 0.4)
    toe_end = short_row_end_stitches(cast_on, 0.3)
    heel_length = short_row_length(cast_on, toe_end, rgauge)

    print "TOE"
    print "Provisional cast on %d stitches." % cast_on
    print "Knit %d stitches until 1 stitch before end, wrap and turn." % (cast_on -1)
    print "Purl %d stitches until 1 stitch before end, wrap and turn." % (cast_on -2)
    print "Knit %d stitches until 1 stitch before first wrapped stitch, wrap and turn." % (cast_on -3)
    print "Purl %d stitches until 1 stitch before first wrapped stitch, wrap and turn." % (cast_on -4)
    print "Continue short rows until %d stitches remain unwrapped.  %d stitches wrapped on each side." % \
          (toe_end, (cast_on - toe_end)/2)
    print "Knit %d, pick up and knit wrap and next stitch together, wrap and turn" % toe_end
    print "Purl %d, pick up and purl wrap and next stitch together, wrap and turn" % (toe_end + 1)
    print "Knit %d, pick up and knit both wraps and next stitch together, wrap and turn" % (toe_end + 2)
    print "Purl %d, pick up and purl both wrap and next stitch together, wrap and turn" % (toe_end + 3)
    print "Continue until all wraps have been consumed."
    print "FOOT"
    print "Pick up provisional stitches and begin knitting in the round.  First half of stitches will be the sole, " \
          "second half will be the instep."
    print "Knit until sock measures %.2f %s." % (foot_length - heel_length, units)
    print "HEEL"
    print "Knit %d stitches until 1 stitch before end of sole stitches, wrap and turn." % (cast_on -1)
    print "Purl %d stitches until 1 stitch before end of sole stitches, wrap and turn." % (cast_on -2)
    print "Knit %d stitches until 1 stitch before first wrapped stitch, wrap and turn." % (cast_on -3)
    print "Purl %d stitches until 1 stitch before first wrapped stitch, wrap and turn." % (cast_on -4)
    print "Continue short rows until %d stitches remain unwrapped.  %d stitches wrapped on each side." % \
          (heel_end, (cast_on - heel_end)/2)
    print "Knit %d, pick up and knit wrap and next stitch together, wrap and turn" % heel_end
    print "Purl %d, pick up and purl wrap and next stitch together, wrap and turn" % (heel_end + 1)
    print "Knit %d, pick up and knit both wraps and next stitch together, wrap and turn" % (heel_end + 2)
    print "Purl %d, pick up and purl both wrap and next stitch together, wrap and turn" % (heel_end + 3)
    print "Continue until all wraps have been consumed."
    print "LEG"
    print "Resume knitting in the round.  Knit until leg is %d %s, or desired length before end ribbing." % \
          (foot_length, units)
    print "Switch to K1P1 or K2P2 ribbing for 1 - 1.5 inches or desired length."
    print "Cast off and weave in ends."

def main():

    pattern()

    #rgauge, sgauge, units = gauge("Inch", 28, 32)
    #print "Gauge is %.2f rows and %.2f stitches per %s" % (sgauge, rgauge, units)

    #cast_on = cast_on_stitches(sgauge, 9, -10)
    #print "Stitches at end of short row toe: ", short_row_end_stitches(cast_on, 0.3), "\n"



if __name__ == '__main__':
    main()