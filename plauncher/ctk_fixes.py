def patch_progressbar_zero():
    try:
        from customtkinter.windows.widgets.core_rendering.draw_engine import DrawEngine
    except Exception:
        return False

    names = (
        ("_DrawEngine__draw_rounded_progress_bar_with_border_polygon_shapes",
         "_DrawEngine__draw_rounded_rect_with_border_polygon_shapes"),
        ("_DrawEngine__draw_rounded_progress_bar_with_border_font_shapes",
         "_DrawEngine__draw_rounded_rect_with_border_font_shapes"),
    )

    for bar_name, bg_name in names:
        if not hasattr(DrawEngine, bar_name) or not hasattr(DrawEngine, bg_name):
            continue
        try:
            setattr(DrawEngine, bar_name, _wrap_progressbar_zero(
                getattr(DrawEngine, bar_name),
                getattr(DrawEngine, bg_name),
            ))
        except Exception:
            continue

    return True


def _wrap_progressbar_zero(orig, draw_bg):
    def patched(self, width, height, corner_radius, border_width,
                inner_corner_radius, v1, v2, orientation):
        try:
            if v1 <= 0 and v2 <= 0:
                if self._canvas.find_withtag("progress_parts"):
                    self._canvas.delete("progress_parts")
                try:
                    return draw_bg(self, width, height, corner_radius,
                                   border_width, inner_corner_radius)
                except TypeError:
                    return draw_bg(self, width, height, corner_radius,
                                   border_width, inner_corner_radius, ())
        except Exception:
            pass
        return orig(self, width, height, corner_radius, border_width,
                    inner_corner_radius, v1, v2, orientation)
    return patched