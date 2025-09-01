{{ $id := .Get 0 }}
{{- if not $id }}
	{{ errorf "The %q shortcode requires a positional ID argument. See %s" .Name .Position }}
{{ end }}
{{- with index site.Data.named_links $id }}
	{{- $text := or ($.Get 1) .name -}}
	[{{ $text }}]({{ .url }})
{{- else }}
	{{ errorf "There is no named link with the id %q. See %s" $id .Position }}
{{ end -}}
