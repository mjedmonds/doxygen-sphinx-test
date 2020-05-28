
.. _program_listing_file_include_javadoc-banner.h:

Program Listing for File javadoc-banner.h
=========================================

|exhale_lsh| :ref:`Return to documentation for file <file_include_javadoc-banner.h>` (``include/javadoc-banner.h``)

.. |exhale_lsh| unicode:: U+021B0 .. UPWARDS ARROW WITH TIP LEFTWARDS

.. code-block:: cpp

   
    void cstyle( int theory );
   
    /*******************************************************************************
     * A brief history of JavaDoc-style (C-style) banner comments.
     *
     * This is the typical JavaDoc-style C-style "banner" comment. It starts with
     * a forward slash followed by some number, n, of asterisks, where n > 2. It's
     * written this way to be more "visible" to developers who are reading the
     * source code.
     *
     * Often, developers are unaware that this is not (by default) a valid Doxygen
     * comment block!
     *
     * However, as long as JAVADOC_BLOCK = YES is added to the Doxyfile, it will
     * work as expected.
     *
     * This style of commenting behaves well with clang-format.
     *
     * @param theory Even if there is only one possible unified theory. it is just a
     *               set of rules and equations.
     ******************************************************************************/
    void javadocBanner( int theory );
   
    /***************************************************************************/
    void doxygenBanner( int theory );
