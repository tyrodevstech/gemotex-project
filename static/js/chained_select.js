$(document).ready(function () {
  var categorySelect = $("#id_category");
  var subcategorySelect = $("#id_subcategory");
  var selectedSubcategoryValue = subcategorySelect.val(); // Remember the selected subcategory

  function loadSubcategories() {
    var categoryId = categorySelect.val();

    if (!categoryId) {
      subcategorySelect.empty().append(
        $("<option>", {
          value: "",
          text: "Select a Category First",
        })
      );
      return; // Exit the function without making the AJAX request
    }

    $.ajax({
      url: "/admin/app_main/productmodel/load_subcategories/",
      data: {
        category_id: categoryId,
      },
      dataType: "json",
      success: function (data) {
        subcategorySelect.empty().append(
          $("<option>", {
            value: "",
            text: "Select a Subcategory",
          })
        );
        $.each(data.subcategories, function (i, subcategory) {
          subcategorySelect.append(
            $("<option>").text(subcategory.name).attr("value", subcategory.id)
          );
        });

        // Re-select the previously selected subcategory if still available
        if (
          selectedSubcategoryValue &&
          subcategorySelect.find(
            'option[value="' + selectedSubcategoryValue + '"]'
          ).length > 0
        ) {
          subcategorySelect.val(selectedSubcategoryValue);
        }
      },
      error: function (xhr, textStatus, errorThrown) {
        console.error("AJAX error:", textStatus, errorThrown);
        subcategorySelect.empty();
      },
    });
  }

  // Load subcategories on page load and category change
  loadSubcategories();

  categorySelect.change(function () {
    loadSubcategories();
  });
});
